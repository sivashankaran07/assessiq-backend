from fastapi import FastAPI
from app.middleware.cors import setup_cors
from app.db.database import Base, engine
# from fastapi.openapi.utils import get_openapi
from fastapi.security import HTTPBearer
# Db
from app.models.user import User  
from app.models.student import Student 
from app.models.classess import Class
from app.models.teacher import Teacher
from app.models.subject import Subject
from app.models.schedule import Schedule
# Routes
from app.routes.auth_route import router as auth_router
from app.routes.student_route import router as student_router
from app.routes.classess_route import router as classess_router
from app.routes.teacher_route import router as teacher_router
from app.routes.subject_route import router as subject_router
from app.routes.schedule_route import router as schedule_router

app = FastAPI(debug=True)
setup_cors(app)

# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema

#     openapi_schema = get_openapi(
#         title="AssessIQ",
#         version="1.0.0",
#         description="API with JWT Auth",
#         routes=app.routes,
#     )
#     openapi_schema["components"]["securitySchemes"] = {
#         "BearerAuth": {
#             "type": "http",
#             "scheme": "bearer",
#             "bearerFormat": "JWT"
#         }
#     }
#     openapi_schema["security"] = [{"BearerAuth": []}]

#     app.openapi_schema = openapi_schema
#     return app.openapi_schema


# app.openapi = custom_openapi
security = HTTPBearer()

Base.metadata.create_all(bind=engine)


app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(student_router, prefix="/student", tags=["Student"])
app.include_router(classess_router, prefix="/classess", tags=["classess"])
app.include_router(teacher_router, prefix="/teacher", tags=["teacher"])
app.include_router(subject_router, prefix="/subject", tags=["subject"])
app.include_router(schedule_router, prefix="/schedule", tags=["schedule"])