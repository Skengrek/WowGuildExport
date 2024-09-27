"""Character activity and equipment table

Revision ID: 07fe4b3d62e6
Revises: 
Create Date: 2024-09-27 16:41:10.642265

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '07fe4b3d62e6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Text(), nullable=False),
    sa.Column('server', sa.Text(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('class', sa.Text(), nullable=True),
    sa.Column('race', sa.Text(), nullable=True),
    sa.Column('faction', sa.Text(), nullable=True),
    sa.Column('gender', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('activities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('activity_id', sa.Text(), nullable=True),
    sa.Column('type', sa.Text(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('character_id', sa.Text(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('equipments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Text(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.Column('mean_item_level', sa.Float(), nullable=True),
    sa.Column('neck_item_id', sa.Text(), nullable=True),
    sa.Column('neck_item_quality', sa.Text(), nullable=True),
    sa.Column('neck_item_level', sa.Integer(), nullable=True),
    sa.Column('shoulder_item_id', sa.Text(), nullable=True),
    sa.Column('shoulder_item_quality', sa.Text(), nullable=True),
    sa.Column('shoulder_item_level', sa.Integer(), nullable=True),
    sa.Column('chest_item_id', sa.Text(), nullable=True),
    sa.Column('chest_item_quality', sa.Text(), nullable=True),
    sa.Column('chest_item_level', sa.Integer(), nullable=True),
    sa.Column('waist_item_id', sa.Text(), nullable=True),
    sa.Column('waist_item_quality', sa.Text(), nullable=True),
    sa.Column('waist_item_level', sa.Integer(), nullable=True),
    sa.Column('legs_item_id', sa.Text(), nullable=True),
    sa.Column('legs_item_quality', sa.Text(), nullable=True),
    sa.Column('legs_item_level', sa.Integer(), nullable=True),
    sa.Column('feet_item_id', sa.Text(), nullable=True),
    sa.Column('feet_item_quality', sa.Text(), nullable=True),
    sa.Column('feet_item_level', sa.Integer(), nullable=True),
    sa.Column('wrist_item_id', sa.Text(), nullable=True),
    sa.Column('wrist_item_quality', sa.Text(), nullable=True),
    sa.Column('wrist_item_level', sa.Integer(), nullable=True),
    sa.Column('hands_item_id', sa.Text(), nullable=True),
    sa.Column('hands_item_quality', sa.Text(), nullable=True),
    sa.Column('hands_item_level', sa.Integer(), nullable=True),
    sa.Column('head_item_id', sa.Text(), nullable=True),
    sa.Column('head_item_quality', sa.Text(), nullable=True),
    sa.Column('head_item_level', sa.Integer(), nullable=True),
    sa.Column('finger_1_item_id', sa.Text(), nullable=True),
    sa.Column('finger_1_item_quality', sa.Text(), nullable=True),
    sa.Column('finger_1_item_level', sa.Integer(), nullable=True),
    sa.Column('finger_2_item_id', sa.Text(), nullable=True),
    sa.Column('finger_2_item_quality', sa.Text(), nullable=True),
    sa.Column('finger_2_item_level', sa.Integer(), nullable=True),
    sa.Column('trinket_1_item_id', sa.Text(), nullable=True),
    sa.Column('trinket_1_item_quality', sa.Text(), nullable=True),
    sa.Column('trinket_1_item_level', sa.Integer(), nullable=True),
    sa.Column('trinket_2_item_id', sa.Text(), nullable=True),
    sa.Column('trinket_2_item_quality', sa.Text(), nullable=True),
    sa.Column('trinket_2_item_level', sa.Integer(), nullable=True),
    sa.Column('back_item_id', sa.Text(), nullable=True),
    sa.Column('back_item_quality', sa.Text(), nullable=True),
    sa.Column('back_item_level', sa.Integer(), nullable=True),
    sa.Column('main_hand_item_id', sa.Text(), nullable=True),
    sa.Column('main_hand_item_quality', sa.Text(), nullable=True),
    sa.Column('main_hand_item_level', sa.Integer(), nullable=True),
    sa.Column('off_hand_item_id', sa.Text(), nullable=True),
    sa.Column('off_hand_item_quality', sa.Text(), nullable=True),
    sa.Column('off_hand_item_level', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('equipments')
    op.drop_table('activities')
    op.drop_table('characters')
    # ### end Alembic commands ###