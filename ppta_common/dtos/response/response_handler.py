from fastapi import FastAPI
from typing import Any, Dict

from .rest_response import RestResponse
from utils.enums import EnumStatusResponse

app = FastAPI()

class ResponseHandler:
    def __init__(self):
        pass

    # GENERATE RESPONSE FOR EXCEPTION
    @staticmethod
    def generate_error(exception: Exception, data=None) -> Dict[str, Any]:
        """
        Génère une réponse d'erreur avec le message de l'exception.
        """
        return RestResponse(data=data, message=f"Erreur : {str(exception)}", status_code=207, status_response=EnumStatusResponse.UNKNOWN)

    # GENERATE RESPONSE FOR NO_CONTENT
    @staticmethod
    def generate_no_content_response(data: any, message: str) -> Dict[str, Any]:
        """
        Génère une réponse sans contenu avec le message fourni.
        """
        return RestResponse(data=data, message=message, status_code=207, status_response=EnumStatusResponse.NO_CONTENT)

    # GENERATE RESPONSE FOR NOT_FOUND
    @staticmethod
    def generate_not_found_response(message: str) -> Dict[str, Any]:
        """
        Génère une réponse de ressource non trouvée avec le message fourni.
        """
        # raise HTTPException(status_code=404, detail=message)
        return RestResponse(data=None, message=message, status_code=404, status_response=EnumStatusResponse.NOT_FOUND)

    # GENERATE RESPONSE FOR NOT_FOUND
    @staticmethod
    def generate_forbidden_response(message: str) -> Dict[str, Any]:
        """
        Génère une réponse de ressource non trouvée avec le message fourni.
        """
        # raise HTTPException(status_code=404, detail=message)
        return RestResponse(data=None, message=message, status_code=403, status_response=EnumStatusResponse.FORBIDDEN)

    # GENERATE OK RESPONSE
    @staticmethod
    def generate_ok_response(data: Any, message: str, status_code: int, status_response: EnumStatusResponse) -> Dict[str, Any]:
        """
        Génère une réponse OK avec le message et les données fournies.
        """
        return RestResponse(data=data, message=message, status_code=status_code, status_response=status_response)