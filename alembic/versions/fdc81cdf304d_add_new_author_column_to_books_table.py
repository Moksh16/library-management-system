"""add new author column to books table

Revision ID: fdc81cdf304d
Revises: 6842fbf78566
Create Date: 2026-04-23 11:46:45.331029

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fdc81cdf304d'
down_revision: Union[str, Sequence[str], None] = '6842fbf78566'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("books", sa.Column("author",sa.String(),nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("books","author")
