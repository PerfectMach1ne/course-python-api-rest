"""free iPhone 5s giveaway

Revision ID: 23cf1f9647ee
Revises: 160ec76e23c3
Create Date: 2023-04-19 12:01:12.266809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23cf1f9647ee'
down_revision = '160ec76e23c3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
