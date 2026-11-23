from . import orders, menu_items


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(menu_items.router)
