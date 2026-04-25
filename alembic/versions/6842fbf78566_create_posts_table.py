"""create posts table

Revision ID: 6842fbf78566
Revises: 3724c8f98c16
Create Date: 2026-04-23 11:25:13.328112

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6842fbf78566'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('books', sa.Column("id",sa.Integer(), nullable=False, primary_key=True), 
                    sa.Column("name", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("books")
