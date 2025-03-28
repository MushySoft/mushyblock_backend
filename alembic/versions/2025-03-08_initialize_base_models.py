"""initialize base models

Revision ID: 138afe722e92
Revises: 4110136247bb
Create Date: 2025-03-08 12:57:40.044144

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '138afe722e92'
down_revision: Union[str, None] = '4110136247bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_trade', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('count', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_item_id'), 'item', ['id'], unique=False)
    op.create_table('line',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('color', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_line_id'), 'line', ['id'], unique=False)
    op.create_table('service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_trade', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_service_id'), 'service', ['id'], unique=False)
    op.create_table('station',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('lng', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_station_id'), 'station', ['id'], unique=False)
    op.create_table('subscription',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_subscription_type', sa.Integer(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.TIMESTAMP(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscription_id'), 'subscription', ['id'], unique=False)
    op.create_table('subscription_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscription_type_id'), 'subscription_type', ['id'], unique=False)
    op.create_table('trade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('seller', sa.Integer(), nullable=True),
    sa.Column('buyer', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Enum('moderate', 'active', 'finished', name='status_enum'), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('finished_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('expires_at', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_trade_id'), 'trade', ['id'], unique=False)
    op.create_table('metro_match',
    sa.Column('id_station', sa.Integer(), nullable=False),
    sa.Column('id_line', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_line'], ['line.id'], ),
    sa.ForeignKeyConstraint(['id_station'], ['station.id'], ),
    sa.PrimaryKeyConstraint('id_station', 'id_line')
    )
    op.add_column('user', sa.Column('id_subscription', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('avatar', sa.String(length=255), nullable=True))
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=12),
               type_=sa.String(length=16),
               existing_nullable=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.String(length=32),
               nullable=True)
    op.alter_column('user', 'name',
               existing_type=sa.VARCHAR(length=12),
               type_=sa.String(length=16),
               nullable=False)
    op.alter_column('user', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('user', 'last_login',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('user', 'balance',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'balance',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('user', 'last_login',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('user', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('user', 'name',
               existing_type=sa.String(length=16),
               type_=sa.VARCHAR(length=12),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.String(length=32),
               type_=sa.VARCHAR(length=16),
               nullable=False)
    op.alter_column('user', 'username',
               existing_type=sa.String(length=16),
               type_=sa.VARCHAR(length=12),
               existing_nullable=False)
    op.drop_column('user', 'avatar')
    op.drop_column('user', 'id_subscription')
    op.drop_table('metro_match')
    op.drop_index(op.f('ix_trade_id'), table_name='trade')
    op.drop_table('trade')
    op.drop_index(op.f('ix_subscription_type_id'), table_name='subscription_type')
    op.drop_table('subscription_type')
    op.drop_index(op.f('ix_subscription_id'), table_name='subscription')
    op.drop_table('subscription')
    op.drop_index(op.f('ix_station_id'), table_name='station')
    op.drop_table('station')
    op.drop_index(op.f('ix_service_id'), table_name='service')
    op.drop_table('service')
    op.drop_index(op.f('ix_line_id'), table_name='line')
    op.drop_table('line')
    op.drop_index(op.f('ix_item_id'), table_name='item')
    op.drop_table('item')
    # ### end Alembic commands ###
