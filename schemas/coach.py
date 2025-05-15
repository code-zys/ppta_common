from schemas.company import companyEntity
from schemas.workplace import workPlaceEntities
from ppta_common.utils.logs import logger


def coachEntity(item, iyvo_coaching_percentage: float, is_public_data: bool = False) -> dict:
    try:
        result = {
            "id": str(item.id),
            "name": item.name,
            "job_title": item.job_title if item.job_title else None,
            "company": companyEntity(item.company) if item.company else None,
            "address": (
                {
                    "country": item.address.country,
                    "city": item.address.city,
                    "street_number": item.address.street_number,
                    "street_name": item.address.street_name,
                    "postal_code": item.address.postal_code,
                }
                if item.address
                else None
            ),
            "slug": item.slug,
            "profile_picture": item.profile_picture,
            "bio": item.bio,
            "languages": [
                {"code": lang.code, "level": lang.level, "titled": lang.titled}
                for lang in item.languages
            ],
            "min_booking_time": item.min_booking_time,
            "member_id": str(item.member_id),
            "is_coaching_profile_visible": item.is_coaching_profile_visible,
            "is_profile_verified": item.is_profile_verified,
            "has_set_up_stripe_connected_account": item.has_set_up_stripe_connected_account,
            "company_approved_coach": item.company_approved_coach,
            "is_profile_disabled_by_admin": item.is_profile_disabled_by_admin,
            "years_of_experience": item.years_of_experience,
            "verified_at": item.verified_at if item.verified_at else None,
            "timezone": (
                {"name": item.timezone.name, "offset": item.timezone.offset}
                if item.timezone
                else None
            ),
            "average_rating": item.average_rating,
            "mission_support": item.mission_support,
            "interview_support": item.interview_support,
            "communication_support": item.communication_support,
            "it_support": item.it_support,
            "other_support": item.other_support,
        }

        if item.interview_support:
            result["interview_workplace"] = workPlaceEntities(item.interview_workplace)
            result["public_interview_another_pricing"] = (
                (
                    item.interview_another_pricing
                    + (
                        item.interview_another_pricing
                        * (iyvo_coaching_percentage / 100)
                    )
                    if item.interview_another_pricing
                    else None
                ),
            )
            result["public_interview_default_pricing"] = (
                item.interview_default_pricing
                + (
                    item.interview_default_pricing
                    * (iyvo_coaching_percentage / 100)
                )
                if item.interview_default_pricing
                else None
            )

        if item.mission_support:
            result["mission_workplace"] = workPlaceEntities(item.mission_workplace)
            result["public_mission_another_pricing"] = (
                item.mission_another_pricing
                + (
                    item.mission_another_pricing
                    * (iyvo_coaching_percentage / 100)
                )
                if item.mission_another_pricing
                else None
            )

            result["public_mission_default_pricing"] = (
                item.mission_default_pricing
                + (
                    item.mission_default_pricing
                    * (iyvo_coaching_percentage / 100)
                )
                if item.mission_default_pricing
                else None
            )

        if item.communication_support:
            result["communication_description"] = item.communication_description
            result["public_communication_another_pricing"] = (
                item.communication_another_pricing
                + (
                    item.communication_another_pricing
                    * (iyvo_coaching_percentage / 100)
                )
                if item.communication_another_pricing
                else None
            )
            result["public_communication_default_pricing"] = (
                item.communication_default_pricing
                + (
                    item.communication_default_pricing
                    * (iyvo_coaching_percentage / 100)
                )
                if item.communication_default_pricing
                else None
            )

        if item.it_support:
            result["it_skills"] = [
                {
                    "name": skill.name,
                    "description": skill.description,
                }
                for skill in item.it_skills
            ]
            result["public_it_another_pricing"] = (
                item.it_another_pricing
                + (item.it_another_pricing * (iyvo_coaching_percentage / 100))
                if item.it_another_pricing
                else None
            )
            result["public_it_default_pricing"] = (
                item.it_default_pricing
                + (item.it_default_pricing * (iyvo_coaching_percentage / 100))
                if item.it_default_pricing
                else None
            )

        if item.other_support:
            result["other_title"] = item.other_title
            result["other_description"] = item.other_description
            result["public_other_another_pricing"] = (
                item.other_another_pricing
                + (item.other_another_pricing * (iyvo_coaching_percentage / 100))
                if item.other_another_pricing
                else None
            )
            result["public_other_default_pricing"] = (
                item.other_default_pricing
                + (item.other_default_pricing * (iyvo_coaching_percentage / 100))
                if item.other_default_pricing
                else None
            )

        if not is_public_data:
            result["email"] = item.email
            result["phone"] = item.phone
            result["mission_another_pricing"] = item.mission_another_pricing
            result["mission_default_pricing"] = item.mission_default_pricing
            result["interview_another_pricing"] = item.interview_another_pricing
            result["interview_default_pricing"] = item.interview_default_pricing
            result["communication_another_pricing"] = item.communication_another_pricing
            result["communication_default_pricing"] = item.communication_default_pricing
            result["it_another_pricing"] = item.it_another_pricing
            result["it_default_pricing"] = item.it_default_pricing
            result["other_another_pricing"] = item.other_another_pricing
            result["other_default_pricing"] = item.other_default_pricing
        return result
    except Exception as exc:
        logger.error(exc)
        raise exc


def coachEntities(entity, is_public_data: bool = False) -> list:
    return [coachEntity(item, is_public_data) for item in entity]


def coachingEntityPaginated(entity, is_public_data: bool = False) -> list:
    if not entity:
        result = []
    else:
        result = coachEntities(entity.items, is_public_data)

    return {
        "items": result,
        "total_items": entity.total_items,
        "total_pages": entity.total_pages,
        "page": entity.page,
        "limit": entity.limit,
    }
