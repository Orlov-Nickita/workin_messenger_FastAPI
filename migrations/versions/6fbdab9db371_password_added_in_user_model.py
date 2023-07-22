"""password added in User model

Revision ID: 6fbdab9db371
Revises: 0b0fb68f8efc
Create Date: 2023-07-22 18:43:38.732333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fbdab9db371'
down_revision = '0b0fb68f8efc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('password_hash', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('User', 'password_hash')
    # ### end Alembic commands ###