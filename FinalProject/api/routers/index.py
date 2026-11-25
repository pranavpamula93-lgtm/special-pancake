from . import orders
from . import customers


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(customers.router)