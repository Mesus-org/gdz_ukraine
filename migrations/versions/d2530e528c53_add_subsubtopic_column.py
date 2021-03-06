"""add subsubtopic column

Revision ID: d2530e528c53
Revises: 77095fa17d31
Create Date: 2020-05-19 08:24:57.528474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2530e528c53'
down_revision = '77095fa17d31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('sub_sub_topic', sa.String(), nullable=True))
    op.add_column('users', sa.Column('sub_topic', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'sub_topic')
    op.drop_column('users', 'sub_sub_topic')
    # ### end Alembic commands ###
