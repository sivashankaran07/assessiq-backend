from app.utils.response import success_response, error_response
from app.core.logger import log_info, log_error
from app.services.student_service import create_student, update_student, list_student, delete_student
from app.core.auth import create_access_token
from app.schemas.student_schema import student_list_response
from app.utils.check_admin import check_admin

def register_student(db, student,current_user):
    check_admin(current_user)
    try:
        new_student = create_student(db, student)
        # token = create_access_token({"sub": student.email,"role": student.role})

        log_info(f"Student created: {new_student.email}")

        return success_response(
            data={
                "id": new_student.id,
                "name": new_student.name,
                "email": new_student.email,
                # "token":token
            },
            message="Student created successfully"
        )

    except Exception as e:
        log_error(f"Error creating student: {str(e)}")

        return error_response(
            message="Failed to create student",
            status_code=500
        )

def update_student_controller(db, student_id, student):
    try:
        updated = update_student(db, student_id, student)

        if not updated:
            return error_response("Student not found", 404)

        return success_response(
            data={"id": updated.id},
            message="Student updated successfully"
        )

    except Exception as e:
        log_error(f"Error updating student: {str(e)}")
        return error_response("Failed to update student", 500)

def get_students(db, skip=0, limit=10):
    try:
        result = list_student(db, skip, limit)

        serialized = student_list_response.model_validate(result).model_dump(mode="json")

        return success_response(
            data=serialized,
            message="Students fetched successfully"
        )

    except Exception as e:
        log_error(f"Error fetching students: {str(e)}")
        return error_response("Failed to fetch students", 500)


def delete_student_controller(db, student_id):
    try:
        deleted = delete_student(db, student_id)

        if not deleted:
            return error_response("Student not found", 404)

        return success_response(
            message="Student deleted successfully"
        )

    except Exception as e:
        log_error(f"Error deleting student: {str(e)}")
        return error_response("Failed to delete student", 500)