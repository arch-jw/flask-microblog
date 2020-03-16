"""added language field to posts table, older scripts are in prev commits

Revision ID: b187bd9a2799
Revises: e877476f777d
Create Date: 2020-03-12 13:58:59.577762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b187bd9a2799'
down_revision = 'e877476f777d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
