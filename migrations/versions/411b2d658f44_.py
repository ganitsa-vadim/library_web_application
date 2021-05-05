"""empty message

Revision ID: 411b2d658f44
Revises: 419dc7a5acf8
Create Date: 2021-05-05 18:15:12.186204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '411b2d658f44'
down_revision = '419dc7a5acf8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('records', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('records', sa.Column('description', sa.TEXT(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('records', 'description')
    op.drop_column('records', 'created_at')
    # ### end Alembic commands ###