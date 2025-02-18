"""Create new class Comment

Revision ID: dfd5b9e79fb8
Revises: 52be54aeef83
Create Date: 2025-01-14 18:00:53.185590

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "dfd5b9e79fb8"
down_revision = "52be54aeef83"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "comment",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("body", sa.String(length=1500), nullable=True),
        sa.Column("data", sa.DateTime(), nullable=True),
        sa.Column("post_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["post.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("comment")
    # ### end Alembic commands ###
