"""next revision

Revision ID: c819b21cbfa9
Revises: 050542e18991
Create Date: 2020-09-20 14:55:18.502270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c819b21cbfa9'
down_revision = '050542e18991'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users',
        Column('full_name', String())
    )


def downgrade():
    pass
