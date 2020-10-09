"""create blogpost table

Revision ID: d3bc35b4160a
Revises: 18bbb936e716
Create Date: 2020-10-09 14:33:38.707310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3bc35b4160a'
down_revision = '18bbb936e716'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.Column('headline', sa.String(255), nullable=False),
        sa.Column('body', sa.Text),
    )


def downgrade():
    op.drop_table('posts')
