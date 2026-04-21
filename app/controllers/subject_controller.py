from sqlalchemy.orm import Session
from app.core.logger import log_info, log_error
from app.services.subject_service import create_subjects, update_subjects, delete_subjects, get_subjects
from app.utils.response import success_response, error_response
from app.utils.check_admin import check_admin
from app.schemas.subject_schema import subject_list_response

def create_subject(db: Session, subject):
    # check_admin(current_user)
    try:
        new_subject = create_subjects(db, subject)
        log_info(f"Subject created: {new_subject.name}")
        return success_response(
            data={
                "id": new_subject.id,
                "name": new_subject.name,
            },
            message="Subject created successfully"
        )
    except Exception as e:
        log_error(f"Error creating subject: {str(e)}")
        return error_response(
            message="Failed to create subject",
            status_code=500
        )

def update_subject(db: Session, subject_id: int, subject):
    try:
        updated = update_subjects(db, subject_id, subject)

        if not updated:
            return error_response("Subject not found", 404)

        return success_response(
            data={"id": updated.id},
            message="Subject updated successfully"
        )

    except Exception as e:
        log_error(f"Error updating subject: {str(e)}")
        return error_response("Failed to update subject", 500)

# def get_subject(db: Session, subject_id: int):
#     try:
#         subject = get_subjects(db, subject_id)

#         if not subject:
#             return error_response("Subject not found", 404)

#         return success_response(
#             data={
#                 "id": subject.id,
#                 "name": subject.name,
#             },
#             message="Subject fetched successfully"
#         )

    except Exception as e:
        log_error(f"Error fetching subject: {str(e)}")
        return error_response("Failed to fetch subject", 500)

def get_all_subjects(db: Session, skip: int = 0, limit: int = 10):
    try:
        result = get_subjects(db, skip, limit)

        serialized = subject_list_response.model_validate(result).model_dump(mode="json")

        return success_response(
            data=serialized,
            message="Subjects fetched successfully"
        )

    except Exception as e:
        log_error(f"Error fetching subjects: {str(e)}")
        return error_response("Failed to fetch subjects", 500)

def delete_subject(db: Session, subject_id: int):
    try:
        deleted = delete_subjects(db, subject_id)

        if not deleted:
            return error_response("Subject not found", 404)

        return success_response(
            message="Subject deleted successfully"
        )

    except Exception as e:
        log_error(f"Error deleting subject: {str(e)}")
        return error_response("Failed to delete subject", 500)