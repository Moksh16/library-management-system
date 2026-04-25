"""create users table

Revision ID: af85a080efe7
Revises: fdc81cdf304d
Create Date: 2026-04-23 13:59:28.287756

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af85a080efe7'
down_revision: Union[str, Sequence[str], None] = 'fdc81cdf304d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("users", sa.Column('id',sa.Integer(), primary_key=True, nullable=False), 
        sa.Column("email", sa.Integer(), nullable=False, unique=True),
        sa.Column("password",sa.String(), nullable=False)
        )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
