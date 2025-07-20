from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import json
import time

class AuditLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        log_data = {
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "process_time": round(process_time, 5)
        }
        # Optionally log additional request info
        # Log to stdout to simulate audit logs
        try:
            # Don't try to serialize the response object or body directly
            print("AUDIT_LOG: " + json.dumps(log_data))
        except Exception as e:
            print(f"AUDIT_LOGGING_ERROR: {str(e)}")
        return response
