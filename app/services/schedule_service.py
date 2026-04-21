from app.models.schedule import Schedule
from sqlalchemy.orm import Session , joinedload
from app.utils.enum_values import ScheduleType
from app.utils.date_format import convert_to_24hr

def create_schedule(db:Session , schedule):

    schedule_type = ScheduleType[schedule.type.upper()]
    # start_time = convert_to_24hr(schedule.start_time)
    # end_time = convert_to_24hr(schedule.end_time)

    if schedule.start_time >= schedule.end_time:
        raise ValueError("End time must be greater than start time")

    conflict = db.query(Schedule).filter(
        Schedule.teacher_id == schedule.teacher_id,
        Schedule.date == schedule.date,
        Schedule.start_time < schedule.end_time,
        Schedule.end_time > schedule.start_time
    ).first()

    if conflict:
        raise ValueError("Teacher already assigned at this time")

    db_schedule = Schedule(
        teacher_id=schedule.teacher_id,
        subject_id=schedule.subject_id,
        class_id=schedule.class_id,
        date=schedule.date,
        start_time=schedule.start_time,
        end_time=schedule.end_time,
        type=schedule_type.value
    )
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def update_schedule(db:Session , schedule_id:int , schedule):
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not db_schedule:
        return None
    update_data = schedule.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_schedule, key, value)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def delete_schedule(db:Session , schedule_id:int):
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not db_schedule:
        return None
    db.delete(db_schedule)
    db.commit()
    return True

def get_schedule(db:Session , schedule_id:int):
    return db.query(Schedule).filter(Schedule.id == schedule_id).options(
        joinedload(Schedule.teacher),
        joinedload(Schedule.class_),
        joinedload(Schedule.subject)
    ).first()

def get_schedules(db:Session , skip:int = 0 , limit:int = 10,class_id: int = None, teacher_id=None,subject_id=None,start_date=None,end_date=None):
    base_query = db.query(Schedule).options(
        joinedload(Schedule.teacher),
        joinedload(Schedule.class_),
        joinedload(Schedule.subject)
        ).order_by(Schedule.id)
 
    if class_id:
        base_query = base_query.filter(Schedule.class_id == class_id)

    if start_date:
        base_query = base_query.filter(Schedule.date >= start_date)

    if end_date:
        base_query = base_query.filter(Schedule.date <= end_date)

    if teacher_id:
        base_query = base_query.filter(Schedule.teacher_id == teacher_id)

    if subject_id:
        base_query = base_query.filter(Schedule.subject_id == subject_id)

    base_query = base_query.order_by(Schedule.date, Schedule.start_time)
    total = base_query.count()
    schedules = base_query.offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": schedules
    }