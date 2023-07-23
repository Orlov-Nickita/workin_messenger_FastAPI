"""well...let`s start again

Revision ID: e3b673eb67c3
Revises: 
Create Date: 2023-07-23 17:24:23.704201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3b673eb67c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Avatar',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('src', sa.String(), nullable=False),
    sa.Column('alt', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Avatar_id'), 'Avatar', ['id'], unique=False)
    op.create_table('User',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('sex', sa.Enum('Man', 'Woman', name='sexenum'), nullable=False),
    sa.Column('avatar_id', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['avatar_id'], ['Avatar.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_User_id'), 'User', ['id'], unique=False)
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
    op.drop_index(op.f('ix_User_id'), table_name='User')
    op.drop_table('User')
    op.drop_index(op.f('ix_Avatar_id'), table_name='Avatar')
    op.drop_table('Avatar')
    # ### end Alembic commands ###