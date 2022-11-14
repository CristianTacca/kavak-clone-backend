"""empty message

Revision ID: 1b095a1023a5
Revises: d1bced5b2a31
Create Date: 2022-11-14 12:01:58.919203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b095a1023a5'
down_revision = 'd1bced5b2a31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cars', sa.Column('cidade', sa.String(length=127), nullable=False))
    op.add_column('cars', sa.Column('estado', sa.String(length=127), nullable=False))
    op.add_column('cars', sa.Column('promocao', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cars', 'promocao')
    op.drop_column('cars', 'estado')
    op.drop_column('cars', 'cidade')
    # ### end Alembic commands ###