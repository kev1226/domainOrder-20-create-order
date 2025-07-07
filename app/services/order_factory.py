import httpx
import os


async def build_order(user_email: str, token: str):
    async with httpx.AsyncClient() as client:
        cart_url = os.getenv("CART_SERVICE_URL")
        clear_url = os.getenv("CLEAR_CART_URL")  # ⚠️ ESTA ES NUEVA

        headers = {"Authorization": f"Bearer {token}"}

        # 1. Obtener carrito
        response = await client.get(cart_url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Error al obtener carrito: {response.text}")

        cart_items = response.json()
        if not cart_items:
            raise Exception("El carrito está vacío")

        # 2. Calcular productos
        detailed_products = []
        total = 0.0
        for item in cart_items:
            price = item["price"]
            quantity = item["quantity"]
            subtotal = round(price * quantity, 2)
            total += subtotal
            detailed_products.append(
                {
                    "product_id": item["product_id"],
                    "name": item["name"],
                    "price_unit": price,
                    "quantity": quantity,
                    "line": f"{price} x {quantity}",
                    "subtotal": subtotal,
                }
            )

        # 3. Limpiar carrito
        clear_response = await client.delete(clear_url, headers=headers)
        if clear_response.status_code != 200:
            raise Exception(
                f"No se pudo limpiar el carrito. Código {clear_response.status_code}"
            )

    # 4. Devolver la orden lista
    return {
        "user": {"email": user_email},
        "products": detailed_products,
        "total": {
            "amount": round(total, 2),
            "currency": "USD",
            "label": "Total general",
        },
        "status": "PENDIENTE_DE_PAGO",
    }
