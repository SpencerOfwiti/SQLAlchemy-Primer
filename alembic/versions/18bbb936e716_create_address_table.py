"""create address table

Revision ID: 18bbb936e716
Revises: 4f80e62cb3b5
Create Date: 2020-10-09 14:21:02.864038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18bbb936e716'
down_revision = '4f80e62cb3b5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'addresses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email_address', sa.String, nullable=False),
        sa.Column('user_id', sa.Integer),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    )


def downgrade():
    op.drop_table('addresses')
