"""create profile and update users table

Revision ID: 5f38bf4a885a
Revises: 23c49938cc8d
Create Date: 2020-09-22 15:33:56.615455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f38bf4a885a'
down_revision = '23c49938cc8d'
branch_labels = None
depends_on = None


def upgrade():

    op.add_column('users',
        sa.Column('provider_type', sa.String()))
    op.add_column('users',
        sa.Column('provider_id', sa.Integer))
    op.add_column('users',
        sa.Column('is_super_user', sa.Boolean))

    op.drop_column('users', 'full_name')


def downgrade():
    pass
