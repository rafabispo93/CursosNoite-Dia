"""empty message

Revision ID: 79bfc9ffcaf3
Revises: 
Create Date: 2017-08-26 20:37:20.969800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79bfc9ffcaf3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario', sa.String(), nullable=True),
    sa.Column('senha', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('usuario')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    # ### end Alembic commands ###