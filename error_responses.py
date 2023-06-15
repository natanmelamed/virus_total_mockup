from fastapi.responses import JSONResponse

NOT_FOUND = {"error": "Not found."}
INVALID_IP = {
    "response_code": -1,
    "verbose_msg": "Invalid IP address"
}


class ErrorResponses:
    @staticmethod
    def get_not_found_error() -> JSONResponse:
        return JSONResponse(
            status_code=404, content=NOT_FOUND)

    @staticmethod
    def get_not_invalid_id_error() -> JSONResponse:
        return \
            JSONResponse(
                status_code=400, content=INVALID_IP)
