from ppta_common.utils.logs import logger


def workPlaceEntity(item) -> dict:
    try:
        result = {
            "code": item.code,
            "client": item.client,
            "description": item.description,
            "position": item.position,
            "skills": [
                {
                    "code": skill.code,
                    "name": skill.name,
                }
                for skill in item.skills
            ],
            "verified": item.verified,
            "start_date": item.start_date,
            "end_date": item.end_date,
            "verified_at": item.verified_at if item.verified_at else None,
        }
        return result
    except Exception as exc:
        logger.error(exc)
        raise exc


def workplace_entities(entity) -> list:
    return [workPlaceEntity(item) for item in entity]


def workplaceEntityPaginated(entity) -> list:
    if not entity:
        result = []
    else:
        result = workPlaceEntity(entity.items)

    return {
        "items": result,
        "total_items": entity.total_items,
        "total_pages": entity.total_pages,
        "page": entity.page,
        "limit": entity.limit,
    }
