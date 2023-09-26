# Import all the models, so that Base has them before being
# imported by Alembic
from models import * # noqa
from db.base import Base  # noqa
