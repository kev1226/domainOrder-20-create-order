from fastapi import Request
from app.services.order_factory import build_order
from app.repository.order_repository import save_order
from app.auth.jwt_utils import decode_token


async def resolve_create_order(_, info):
    request: Request = info.context["request"]
    auth_header = request.headers.get("Authorization", "").replace("Bearer ", "")
    token = auth_header.strip()
    user_data = decode_token(token)

    if not user_data:
        raise Exception("Token inválido")

    email = user_data["email"]
    order = await build_order(email, token)
    saved_order = await save_order(order)

    return {
        "id": saved_order["id"],
        "status": saved_order["status"],
        "message": "Orden creada correctamente",
    }
