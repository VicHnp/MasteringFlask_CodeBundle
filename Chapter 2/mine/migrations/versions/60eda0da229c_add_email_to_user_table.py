"""add email to User table

Revision ID: 60eda0da229c
Revises: 
Create Date: 2017-03-17 23:58:19.703852

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60eda0da229c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
