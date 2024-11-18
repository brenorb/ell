"""correcting incorrect unique constraint specification

Revision ID: 17ff4eaabe85
Revises: 4524fb60d23e
Create Date: 2024-11-18 21:08:45.321668+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17ff4eaabe85'
down_revision: Union[str, None] = '4524fb60d23e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uq_serializedlmp_version_number_name', 'serializedlmp', ['version_number', 'name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_serializedlmp_version_number_name', 'serializedlmp', type_='unique')
    # ### end Alembic commands ###
