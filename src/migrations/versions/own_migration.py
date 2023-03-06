"""added new field

Revision ID: da886d1119c5
Revises: 348bfeb0a354
Create Date: 2023-03-02 16:50:01.783376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import text

revision = 'da886d1119c6'
down_revision = 'da886d1119c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    conn.execute(
        text(
            """
                UPDATE films
                SET test = 100
                WHERE title like '%Deathly%'
            """
        )
    )

    # ### end Alembic commands ###


def downgrade():
    conn = op.get_bind()
    conn.execute(
        text(
            """
                UPDATE films
                SET test = NULL
                WHERE title like '%Deathly%'
            """
        )
    )