from bson import ObjectId
from datetime import datetime

from ppta_common.models.coach import Coach
from ppta_common.models.company import Company
from ppta_common.dtos.response.orchestration_result import OrchestrationResult
from ppta_common.dtos.response.enum_response import EnumStatusCode
from ppta_common.models.language import Language
from ppta_common.models.address import Address
from ppta_common.models.timezone import TimeZone
from ppta_common.models.workplace import Workplace
from ppta_common.models.skill import Skill
from ppta_common.models.basic_skill import BasicSkill
from ppta_common.models.member_info import MemberInfo
from ppta_common.dtos.request.user_dto import UserDtoMetadata
from ppta_common.dtos.request.coach_create_dto import CoachCreationDto

from ppta_common.utils.logs import logger
from ppta_common.utils.utils import Utils
from slugify import slugify

from ppta_common.schemas.coach import coachEntity

class CoachService:
    """
    Service class for handling coach-related operations.
    """

    @staticmethod
    def create_coach(
        company: Company,
        payload: CoachCreationDto,
        current_user: UserDtoMetadata,
        member_id: str,
        min_price: float,
        mininum_coach_booking_time: int,
        iyvo_coaching_percentage: float
    ) -> OrchestrationResult:
        """
        Create a new coach.
        """
        try:
            # Check if the coach already exists
            existing_coach: Coach = Coach.objects(
                member_id=member_id, deleted=False
            ).first()
            if existing_coach:
                return OrchestrationResult.Failure(
                    "Coach with this email or phone already exists",
                    EnumStatusCode.ALREADY_EXIST,
                )

            # Create a new coach
            coach: Coach = Coach()
            coach.name = payload.name
            coach.email = payload.email
            coach.phone = payload.phone
            coach.years_of_experience = payload.years_of_experience
            coach.languages = (
                [Language(**lang.model_dump()) for lang in payload.languages]
                if payload.languages
                else []
            )
            coach.min_booking_time = mininum_coach_booking_time
            coach.is_coaching_profile_visible = payload.is_coaching_profile_visible
            coach.bio = payload.bio
            coach.address = (
                Address(**payload.address.model_dump()) if payload.address else None
            )
            coach.profile_picture = payload.profile_picture
            coach.job_title = payload.job_title
            coach.timezone = (
                TimeZone(**payload.timezone.model_dump())
                if payload.timezone
                else company.timeZone
            )

            if payload.mission_support:
                coach.mission_support = payload.mission_support
                if payload.mission_workplace:
                    workplaces = []
                    for wp in payload.mission_workplace:
                        worpl = Workplace()
                        worpl.client = wp.client
                        worpl.code = slugify(wp.client)
                        worpl.position = wp.position
                        worpl.description = wp.description
                        worpl.start_date = wp.start_date
                        worpl.end_date = wp.end_date
                        worpl.skills = (
                            [Skill(**skill.model_dump()) for skill in wp.skills]
                            if wp.skills
                            else []
                        )
                        workplaces.append(worpl)
                    coach.mission_workplace = workplaces

                coach.mission_another_pricing = payload.mission_another_pricing
                coach.mission_default_pricing = Utils.check_min_price(
                    payload.mission_default_pricing,
                    min_price
                )

            if payload.interview_support:
                coach.interview_support = payload.interview_support
                if payload.interview_workplace:
                    workplaces = []
                    for wp in payload.interview_workplace:
                        worpl = Workplace()
                        worpl.client = wp.client
                        worpl.code = slugify(wp.client)
                        worpl.position = wp.position
                        worpl.description = wp.description
                        worpl.start_date = wp.start_date
                        worpl.end_date = wp.end_date
                        worpl.skills = (
                            [Skill(**skill.model_dump()) for skill in wp.skills]
                            if wp.skills
                            else []
                        )
                        workplaces.append(worpl)
                    coach.interview_workplace = workplaces

                coach.interview_another_pricing = payload.interview_another_pricing
                coach.interview_default_pricing = payload.interview_default_pricing

            if payload.communication_support:
                coach.communication_support = payload.communication_support
                coach.communication_description = payload.communication_description
                coach.communication_another_pricing = (
                    payload.communication_another_pricing
                )
                coach.communication_default_pricing = Utils.check_min_price(
                    payload.communication_default_pricing,
                    min_price
                )

            if payload.it_support:
                coach.it_support = payload.it_support
                if payload.it_skills:
                    it_skills = []
                    for skill in payload.it_skills:
                        it_skill = BasicSkill()
                        it_skill.name = skill.name
                        it_skill.description = skill.description
                        it_skills.append(it_skill)
                    coach.it_skills = it_skills

                coach.it_another_pricing = payload.it_another_pricing
                coach.it_default_pricing = Utils.check_min_price(
                    payload.it_default_pricing,
                    min_price
                )

            if payload.other_support:
                coach.other_support = payload.other_support
                coach.other_title = payload.other_title
                coach.other_description = payload.other_description
                coach.other_another_pricing = payload.other_another_pricing
                coach.other_default_pricing = Utils.check_min_price(
                    payload.other_default_pricing,
                    min_price
                )

            coach.member_id = member_id
            coach.is_profile_verified = False
            coach.is_profile_disabled_by_admin = False
            coach.company = company

            coach.created_by = Utils.construct_user_meta_data(current_user)
            coach.created_at = Utils.convert_date_in_gmt_and_timstamp(datetime.now())

            coach.slug = slugify(payload.name)
            try:
                # recuperer le dernier coach ayant le meme slug
                existing_slug = (
                    Coach.objects(slug__icontains=coach.slug, deleted=False)
                    .order_by("-created_at")
                    .first()
                )
            except Exception as e:
                existing_slug = None
                logger.error(f"Error while checking existing slug: {e}")

            if existing_slug:
                coach.slug = Utils.generate_next_slug(str(existing_slug.slug))

            coach.save()
            
            return OrchestrationResult.Success(
                EnumStatusCode.CREATED_SUCCESSFULLY, coachEntity(coach, iyvo_coaching_percentage)
            )
        except Exception as e:
            logger.error(e)
            return OrchestrationResult.Failure(str(e), EnumStatusCode.UNKNOWN)