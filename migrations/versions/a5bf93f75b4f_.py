"""empty message

Revision ID: a5bf93f75b4f
Revises: 4c32a835f079
Create Date: 2019-04-15 15:41:16.881150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5bf93f75b4f'
down_revision = '4c32a835f079'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('username', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_comment_username'), 'comment', ['username'], unique=True)
    op.add_column('post', sa.Column('username', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_post_username'), 'post', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_username'), table_name='post')
    op.drop_column('post', 'username')
    op.drop_index(op.f('ix_comment_username'), table_name='comment')
    op.drop_column('comment', 'username')
    # ### end Alembic commands ###
