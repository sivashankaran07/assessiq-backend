from sqlalchemy.orm import Session
from app.utils.response import success_response, error_response
from app.core.logger import log_info, log_error
from app.services.classess_service import create_class, update_class, list_class, delete_class
# from app.core.auth import create_access_token
from app.utils.check_admin import check_admin
from app.schemas.classess_schema import ClassListResponse


def register_class(db: Session, Classess, current_user):
    check_admin(current_user)
    try:
        new_class = create_class(db, Classess)
        log_info(f"Class created: {new_class.name}")
        return success_response(
            data={
                "id": new_class.id,
                "name": new_class.name,
                "section": new_class.section,
            },
            message="Class created successfully"
        )
    except Exception as e:
        log_error(f"Error creating class: {str(e)}")

        return error_response(
            message="Failed to create class",
            status_code=500
        )


def update_class_controller(db: Session, class_id, Classess, current_user):
    check_admin(current_user)
    try:
        updated_class = update_class(db, class_id, Classess)
        if not updated_class:
            return error_response("Class not found", 404)
        return success_response(
            data={
                "id": updated_class.id,
                "name": updated_class.name,
                "section": updated_class.section,
            },
            message="Class updated successfully"
        )
    except Exception as e:
        log_error(f"Error updating class: {str(e)}")
        return error_response(
            message="Failed to update class",
            status_code=500
        )


def get_classes(db: Session, current_user, skip:0, limit:10):
    check_admin(current_user)
    try:
        result = list_class(db, skip, limit)

        serialized_data = ClassListResponse.model_validate(result).model_dump(mode="json")
        return success_response(
            data=serialized_data,
            message="Classes fetched successfully"
        )
    except Exception as e:
        log_error(f"Error fetching classes: {str(e)}")
        return error_response(
            message="Failed to fetch classes",
            status_code=500
        )


def delete_class_controller(db: Session,current_user , class_id):
    check_admin(current_user)
    try:
        deleted = delete_class(db, class_id)
        if not deleted:
            return error_response("Class not found", 404)
        return success_response(
            message="Class deleted successfully"
        )
    except Exception as e:
        log_error(f"Error deleting class: {str(e)}")
        return error_response(
            message="Failed to delete class",
            status_code=500
        )