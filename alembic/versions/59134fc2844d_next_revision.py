"""next revision

Revision ID: 59134fc2844d
Revises: c819b21cbfa9
Create Date: 2020-09-20 22:30:43.902313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59134fc2844d'
down_revision = 'c819b21cbfa9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users',
        sa.Column('full_name', sa.String())
    )


def downgrade():
    pass
