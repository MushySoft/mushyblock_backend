"""rename user table

Revision ID: f8e27d819d84
Revises: f8e04f7f22ff
Create Date: 2025-03-18 21:07:44.086742

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f8e27d819d84'
down_revision: Union[str, None] = 'f8e04f7f22ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=16), nullable=False),
    sa.Column('email', sa.String(length=32), nullable=True),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=16), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('last_login', sa.TIMESTAMP(), nullable=False),
    sa.Column('id_subscription', sa.Integer(), nullable=False),
    sa.Column('balance', sa.Float(), nullable=False),
    sa.Column('avatar', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['id_subscription'], ['subscription.id'], name='fk_user_subscription'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id_subscription'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.drop_index('ix_user_id', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=16), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('hashed_password', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=16), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('last_login', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('balance', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('id_subscription', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('avatar', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_subscription'], ['subscription.id'], name='fk_user_subscription'),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key'),
    sa.UniqueConstraint('id_subscription', name='user_id_subscription_key'),
    sa.UniqueConstraint('username', name='user_username_key')
    )
    op.create_index('ix_user_id', 'user', ['id'], unique=False)
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
