from app.services.schedule_service import create_schedule , update_schedule , delete_schedule , get_schedule , get_schedules
from app.utils.response import success_response, error_response
from app.core.logger import log_info, log_error
from app.schemas.schedule_schema import schedule_list_response
from app.utils.check_admin import check_admin

def create_schedule_controller(db, schedule):
    # check_admin(current_user)
    try:
        new_schedule = create_schedule(db, schedule)
        log_info(f"Schedule created: {new_schedule.id}")
        return success_response(
            data={
                "id": new_schedule.id,
                "teacher_id": new_schedule.teacher_id,
                "subject_id": new_schedule.subject_id,
                "class_id": new_schedule.class_id,
                "date": str(new_schedule.date),
                "start_time": str(new_schedule.start_time),
                "end_time": str(new_schedule.end_time),
                "type": new_schedule.type
            },
            message="Schedule created successfully"
        )
    except Exception as e:
        log_error(f"Error creating schedule: {str(e)}")
        return error_response(
            message=str(e),
            status_code=500
        )

def update_schedule_controller(db, schedule_id, schedule):
    # check_admin(current_user)
    try:
        updated = update_schedule(db, schedule_id, schedule)
        if not updated:
            return error_response("Schedule not found", 404)
        log_info(f"Schedule updated: {updated.id}")
        return success_response(
            data={
                "id": updated.id,
                "teacher_id": updated.teacher_id,
                "subject_id": updated.subject_id,
                "class_id": updated.class_id,
                "date": updated.date,
                "start_time": updated.start_time,
                "end_time": updated.end_time,
                "type": updated.type
            },
            message="Schedule updated successfully"
        )
    except Exception as e:
        log_error(f"Error updating schedule: {str(e)}")
        return error_response(
            message="Failed to update schedule",
            status_code=500
        )

def delete_schedule_controller(db, schedule_id):
    # check_admin(current_user)
    try:
        deleted = delete_schedule(db, schedule_id)
        if not deleted:
            return error_response("Schedule not found", 404)
        log_info(f"Schedule deleted: {schedule_id}")
        return success_response(
            message="Schedule deleted successfully"
        )
    except Exception as e:
        log_error(f"Error deleting schedule: {str(e)}")
        return error_response(
            message="Failed to delete schedule",
            status_code=500
        )

def get_schedule_controller(db, schedule_id):
    # check_admin(current_user)
    try:
        schedule = get_schedule(db, schedule_id)
        if not schedule:
            return error_response("Schedule not found", 404)
        log_info(f"Schedule fetched: {schedule.id}")
        return success_response(
            data={
                "id": schedule.id,
                "teacher_id": schedule.teacher_id,
                "subject_id": schedule.subject_id,
                "class_id": schedule.class_id,
                "date": schedule.date,
                "start_time": schedule.start_time,
                "end_time": schedule.end_time,
                "type": schedule.type
            },
            message="Schedule fetched successfully"
        )
    except Exception as e:
        log_error(f"Error fetching schedule: {str(e)}")
        return error_response(
            message="Failed to fetch schedule",
            status_code=500
        )

def get_schedules_controller(db, skip=0, limit=10, current_user=None,class_id= None, teacher_id=None,subject_id=None,start_date=None,end_date=None):
    try:
        result = get_schedules(db, skip, limit,class_id,teacher_id,subject_id,start_date,end_date)
        serialized = schedule_list_response.model_validate(result).model_dump(mode="json")
        log_info(f"Schedules fetched: {result['total']}")
        return success_response(
            data=serialized,
            message="Schedules fetched successfully"
        )
    except Exception as e:
        log_error(f"Error fetching schedules: {str(e)}")
        return error_response(
            message="Failed to fetch schedules",
            status_code=500
        )