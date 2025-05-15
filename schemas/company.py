from ppta_common.models.company import Company
from ppta_common.utils.logs import logger


def my_entity(item) -> dict:
    try:
        result = {
            "id": str(item.id),
            "siret": item.siret,
            "name": item.name,
            "activity": item.activity,
            "email": item.email,
            "phone": item.phone,
            "type": item.type,
            "logo": item.logo,
            "billing_email": item.billing_email,
            "start_activity_date": item.start_activity_date,
            "member_count": item.member_count if item.member_count else 0,
            "use_contact_as_billing_info": item.use_contact_as_billing_info,
            "created_at": item.created_at,
            "updated_at": item.updated_at,
            "subscription_id": item.subscription_id,
        }

        if item.address:
            result["address"] = {
                "country": item.address.country,
                "city": item.address.city,
                "street_number": item.address.street_number,
                "street_name": item.address.street_name,
                "postal_code": item.address.postal_code,
            }

        if item.timeZone:
            result["timeZone"] = {
                "name": item.timeZone.name,
                "offset": item.timeZone.offset,
            }
        if item.billing_address:
            result["billing_address"] = {
                "country": item.billing_address.country,
                "city": item.billing_address.city,
                "street_number": item.billing_address.street_number,
                "street_name": item.billing_address.street_name,
                "postal_code": item.billing_address.postal_code,
            }
        else:
            result["billing_address"] = None
        if item.created_by:
            result["created_by"] = {
                "id": item.created_by.id,
                "fullname": item.created_by.fullname,
                "picture": item.created_by.picture,
                "user_id": item.created_by.user_id,
                "email": item.created_by.email,
            }
        else:
            result["created_by"] = None
        if item.updated_by:
            result["updated_by"] = {
                "id": item.updated_by.id,
                "fullname": item.updated_by.fullname,
                "picture": item.updated_by.picture,
                "user_id": item.updated_by.user_id,
                "email": item.updated_by.email,
            }
        else:
            result["updated_by"] = None
        return result
    except Exception as exc:
        logger.error(exc)
        raise exc


def companiesEntity(entity) -> list:
    return [my_entity(item) for item in entity]


def previewCompanyEntity(entity: Company) -> dict:
    company_dict = entity.to_dict()
    return {
        "id": company_dict["id"],
        "name": company_dict["name"],
        "siret": company_dict["siret"],
        "activity": company_dict["activity"],
    }


def partialCompanyEntity(item) -> dict:
    return {
        "id": str(item.id),
        "name": item.name,
        "type": item.type,
        "logo": item.logo,
        "currency": item.currency,
    }


def previewCompaniesEntity(entity) -> list:
    return [previewCompanyEntity(item) for item in entity]


def companyEntity(entity) -> dict:
    return my_entity(entity)


def companiesEntityPaginated(entity) -> dict:
    if not entity:
        result = []
    else:
        result = companiesEntity(entity.items)
    return {
        "items": result,
        "total_items": entity.total_items,
        "total_pages": entity.total_pages,
        "page": entity.page,
        "limit": entity.limit,
    }
