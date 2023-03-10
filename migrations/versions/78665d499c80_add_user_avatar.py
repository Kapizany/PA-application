"""add user avatar

Revision ID: 78665d499c80
Revises: b6db2042b821
Create Date: 2023-02-05 13:04:46.009395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78665d499c80'
down_revision = 'b6db2042b821'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('avatar_path', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_model', schema=None) as batch_op:
        batch_op.drop_column('avatar_path')

    # ### end Alembic commands ###
