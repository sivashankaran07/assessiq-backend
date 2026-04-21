from app.utils.response import success_response, error_response
from app.core.logger import log_info, log_error
from app.services.teacher_service import create_teacher, update_teacher, list_teacher, delete_teacher
from app.core.auth import create_access_token
from app.schemas.teacher_schema import teacher_list_response
from app.utils.check_admin import check_admin

def register_teacher(db, teacher):
    # check_admin(current_user)
    try:
        new_teacher = create_teacher(db, teacher)
        # token = create_access_token({"sub": teacher.email,"role": teacher.role})

        log_info(f"Teacher created: {new_teacher.email}")

        return success_response(
            data={
                "id": new_teacher.id,
                "name": new_teacher.name,
                "email": new_teacher.email,
                # "token":token
            },
            message="Teacher created successfully"
        )

    except Exception as e:
        log_error(f"Error creating teacher: {str(e)}")

        return error_response(
            message="Failed to create teacher",
            status_code=500
        )

def update_teacher_controller(db, teacher_id, teacher):
    try:
        updated = update_teacher(db, teacher_id, teacher)

        if not updated:
            return error_response("Teacher not found", 404)

        return success_response(
            data={"id": updated.id},
            message="Teacher updated successfully"
        )

    except Exception as e:
        log_error(f"Error updating teacher: {str(e)}")
        return error_response("Failed to update teacher", 500)

def get_teachers(db, skip=0, limit=10):
    try:
        result = list_teacher(db, skip, limit)

        serialized = teacher_list_response.model_validate(result).model_dump(mode="json")

        return success_response(
            data=serialized,
            message="Teachers fetched successfully"
        )

    except Exception as e:
        log_error(f"Error fetching teachers: {str(e)}")
        return error_response("Failed to fetch teachers", 500)

def delete_teacher_controller(db, teacher_id):
    try:
        deleted = delete_teacher(db, teacher_id)

        if not deleted:
            return error_response("Teacher not found", 404)

        return success_response(
            message="Teacher deleted successfully"
        )

    except Exception as e:
        log_error(f"Error deleting teacher: {str(e)}")
        return error_response("Failed to delete teacher", 500)