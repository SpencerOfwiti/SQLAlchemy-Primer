"""create user table

Revision ID: 4f80e62cb3b5
Revises: 
Create Date: 2020-10-09 12:46:40.444869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f80e62cb3b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('fullname', sa.String),
        sa.Column('nickname', sa.String),
    )


def downgrade():
    op.drop_table('users')
