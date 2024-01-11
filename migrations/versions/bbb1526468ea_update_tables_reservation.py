"""update tables reservation

Revision ID: bbb1526468ea
Revises: 3d2af359fab5
Create Date: 2024-01-11 16:37:20.409886

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bbb1526468ea'
down_revision = '3d2af359fab5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nomor', sa.String(length=120), nullable=False))
        batch_op.drop_column('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', mysql.VARCHAR(length=120), nullable=False))
        batch_op.drop_column('nomor')

    # ### end Alembic commands ###