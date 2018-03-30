"""Promises table

Revision ID: 6ed54c9f6773
Revises: 0b10258919c7
Create Date: 2018-03-30 13:19:48.606786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ed54c9f6773'
down_revision = '0b10258919c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('promise',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('body', sa.String(length=128), nullable=True),
    sa.Column('actionable', sa.Boolean(), nullable=True),
    sa.Column('state', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_promise_actionable'), 'promise', ['actionable'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_promise_actionable'), table_name='promise')
    op.drop_table('promise')
    # ### end Alembic commands ###
