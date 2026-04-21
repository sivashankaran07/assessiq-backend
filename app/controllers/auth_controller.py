from app.services.auth_service import create_user, authenticate_user
from app.core.auth import create_access_token
from app.utils.response import success_response, error_response
from app.core.logger import log_info, log_error

def register_controller(db, user):
    new_user = create_user(db, user)
    log_info("User registered")
    return success_response(
        data={"id": new_user.id, "email": new_user.email},
        message="User created"
    )


def login_controller(db, user):
    db_user = authenticate_user(db, user.email, user.password)

    if not db_user:
        log_error(f"Login failed for email: {user.email}")
        return error_response("Invalid credentials", 401)

    token = create_access_token({"sub": db_user.email,"role": db_user.role})
    
    log_info(f"User logged in: {user.email}") 
    return success_response(
        data={"access_token": token, "role": db_user.role},
        message="Login successful"
    )