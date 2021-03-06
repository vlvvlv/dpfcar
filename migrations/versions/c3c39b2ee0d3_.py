"""empty message

Revision ID: c3c39b2ee0d3
Revises: 
Create Date: 2021-01-08 07:58:30.078779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3c39b2ee0d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dpfcar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('carnumber', sa.String(length=15), nullable=False),
    sa.Column('carnumber4', sa.String(length=4), nullable=False),
    sa.Column('caryear', sa.String(length=4), nullable=False),
    sa.Column('carkind', sa.String(length=10), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('carnumber')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.String(length=50), nullable=False),
    sa.Column('userpassword', sa.String(length=200), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('usertel', sa.String(length=50), nullable=False),
    sa.Column('useremail', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('useremail'),
    sa.UniqueConstraint('userid')
    )
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dpfcar_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('ownername', sa.String(length=100), nullable=False),
    sa.Column('ownertel', sa.String(length=50), nullable=False),
    sa.Column('owneretc', sa.Text(), nullable=True),
    sa.Column('licenseimg', sa.BLOB(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['dpfcar_id'], ['dpfcar.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact')
    op.drop_table('user')
    op.drop_table('dpfcar')
    # ### end Alembic commands ###
