"""empty message

Revision ID: c5344db1ef47
Revises: c3c39b2ee0d3
Create Date: 2021-01-08 23:22:58.445669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5344db1ef47'
down_revision = 'c3c39b2ee0d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dpfcar', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_dpfcar_carnumber'), ['carnumber'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_useremail'), ['useremail'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_userid'), ['userid'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_userid'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_useremail'), type_='unique')

    with op.batch_alter_table('dpfcar', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_dpfcar_carnumber'), type_='unique')

    # ### end Alembic commands ###