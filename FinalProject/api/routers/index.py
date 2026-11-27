from . import orders, menu_items, promotions


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(menu_items.router)
    app.include_router(promotions.router)
