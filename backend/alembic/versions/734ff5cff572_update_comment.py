"""update_comment

Revision ID: 734ff5cff572
Revises: e00669d408d3
Create Date: 2024-12-08 11:33:20.746689

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '734ff5cff572'
down_revision: Union[str, None] = 'e00669d408d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('token_comments', sa.Column('img_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('token_comments', 'img_url')
    # ### end Alembic commands ###
