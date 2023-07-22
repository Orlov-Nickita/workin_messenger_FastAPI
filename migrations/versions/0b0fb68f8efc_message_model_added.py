"""Message model added

Revision ID: 0b0fb68f8efc
Revises: 53f9a7b76412
Create Date: 2023-07-22 15:47:11.850383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b0fb68f8efc'
down_revision = '53f9a7b76412'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Message',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('recipient_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['recipient_id'], ['User.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Message_id'), 'Message', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Message_id'), table_name='Message')
    op.drop_table('Message')
    # ### end Alembic commands ###