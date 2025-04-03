from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

class TokenAuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, valid_token: str):
        super().__init__(app)
        self.valid_token = valid_token

    async def dispatch(self, request: Request, call_next):
        # Only check token for the /data route
        if request.url.path == "/data" and request.method == "POST":
            try:
                # Check for Authorization header
                auth_header = request.headers.get("Authorization")
                if not auth_header:
                    return JSONResponse(
                        status_code=401,
                        content={"detail": "Missing Authorization header"}
                    )
                
                # Validate the token (no Bearer prefix checking)
                if auth_header != self.valid_token:
                    return JSONResponse(
                        status_code=401,
                        content={"detail": "Invalid token"}
                    )
                    
            except Exception as e:
                # Catch any other exceptions that might occur
                return JSONResponse(
                    status_code=500,
                    content={"detail": f"Internal server error: {str(e)}"}
                )
        
        # Proceed with the request if everything is fine
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            # Handle any exceptions that might occur during request processing
            return JSONResponse(
                status_code=500,
                content={"detail": f"Internal server error: {str(e)}"}
            )