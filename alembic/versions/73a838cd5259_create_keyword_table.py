"""create keyword table

Revision ID: 73a838cd5259
Revises: d3bc35b4160a
Create Date: 2020-10-09 14:41:11.727556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73a838cd5259'
down_revision = 'd3bc35b4160a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'keywords',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('keyword', sa.String(50), nullable=False, unique=True),
    )


def downgrade():
    op.drop_table('keywords')
