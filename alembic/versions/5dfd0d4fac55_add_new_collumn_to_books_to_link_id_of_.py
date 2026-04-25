"""add new collumn to books to link id of users

Revision ID: 5dfd0d4fac55
Revises: af85a080efe7
Create Date: 2026-04-23 17:46:57.116436

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5dfd0d4fac55'
down_revision: Union[str, Sequence[str], None] = 'af85a080efe7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("books", sa.Column("owner_id", sa.Integer(),nullable=False))
    op.create_foreign_key('books_users_fk',source_table="books",referent_table="users", local_cols=['owner_id'],
        remote_cols=['id'], ondelete=['CASCADE'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constaint("book_users_fk", table_name="books")
    op.drop_column('posts','owner_id')
