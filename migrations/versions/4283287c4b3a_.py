"""empty message

Revision ID: 4283287c4b3a
Revises: c5344db1ef47
Create Date: 2021-01-09 13:22:11.882603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4283287c4b3a'
down_revision = 'c5344db1ef47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ownernum4', sa.String(length=4), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact', schema=None) as batch_op:
        batch_op.drop_column('ownernum4')

    # ### end Alembic commands ###