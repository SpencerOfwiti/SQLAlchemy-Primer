"""create postkeywords table

Revision ID: 8aebae28782d
Revises: 73a838cd5259
Create Date: 2020-10-09 14:45:40.557094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8aebae28782d'
down_revision = '73a838cd5259'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'post_keywords',
        sa.Column('post_id', sa.Integer, primary_key=True),
        sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
        sa.Column('keyword_id', sa.Integer, primary_key=True),
        sa.ForeignKeyConstraint(['keyword_id'], ['keywords.id'], ),
    )


def downgrade():
    op.drop_table('post_keywords')
