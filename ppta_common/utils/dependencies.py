from fastapi import Header, HTTPException, Request
from jose import jwt, JWTError
from ppta_common.dtos.request.user_dto import UserDtoMetadata
from ppta_common.models.member_info import MemberInfo
from starlette import status
from typing import List, Optional

from utils.enums import EnumRole

def get_current_user_dependency(secret_key: str, algorithm: str):
    async def get_current_user(authorization: Optional[str] = Header(None)) -> UserDtoMetadata:
        """
        Dependency to extract and validate the current user from a JWT token.

        :param authorization: Bearer token from the Authorization header.
        :return: UserDtoMetadata object.
        """
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        if not authorization:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authorization header is missing",
            )
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authorization scheme",
            )
        try:
            payload = jwt.decode(token, secret_key, algorithms=[algorithm])
            if payload and not payload["disabledByAdmin"] and payload["enabled"]:
                user = UserDtoMetadata(**payload)
                return user
            raise credentials_exception
        except JWTError as err:
            raise credentials_exception from err

    return get_current_user


def get_member_info_dependency(secret_key: str, algorithm: str):
    def dependency(
        allowed_roles: List[EnumRole] = [],
        company_token: str = Header(..., alias="CompanyToken"),
        request: Request = None
    ) -> MemberInfo:
        """
        Dependency to validate company tokens and extract member information.

        :param allowed_roles: List of allowed roles for the operation.
        :param company_token: JWT token from the CompanyToken header.
        :param request: HTTP request object.
        :return: MemberInfo object.
        """
        try:
            payload = jwt.decode(company_token, secret_key, algorithms=[algorithm])
            company_id = payload.get("companyId")
            user_id = payload.get("userId")
            role = payload.get("role")
            member_id = payload.get("memberId")
            member_info = MemberInfo(companyId=company_id, userId=user_id, role=role, memberId=member_id)
        except JWTError as e:
            raise HTTPException(status_code=401, detail="Invalid token") from e

        token_company_id = payload.get("companyId")
        if not token_company_id:
            raise HTTPException(status_code=401, detail="Token does not contain companyId")

        url_company_id = request.path_params.get("company_id")
        if (str(token_company_id) != str(url_company_id)) and len(str(url_company_id)) > 0:
            raise HTTPException(status_code=403, detail="Forbidden: companyId does not match")

        if role not in allowed_roles and len(allowed_roles) > 0:
            raise HTTPException(status_code=403, detail="Forbidden: insufficient permissions")

        return member_info

    return dependency
