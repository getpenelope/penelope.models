"""add ticket summary

Revision ID: 2ef36286d521
Revises: 47fb94ed7f66
Create Date: 2014-01-27 16:34:43.857283

"""

# revision identifiers, used by Alembic.
revision = '2ef36286d521'
down_revision = '47fb94ed7f66'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm.session import Session
from penelope.models import TimeEntry


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('time_entries', sa.Column('tickettitle', sa.Unicode(), nullable=True))
    context = op.get_context()
    session = Session()
    session.bind = context.bind

    for tp in session.query(TimeEntry):
        for trac in tp.project.tracs:
            ticket = session.execute('select summary from "trac_%s".ticket where id=%s' % (trac.trac_name, tp.ticket)).fetchone()
            tp.tickettitle = ticket.summary
    session.commit()
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('time_entries', 'tickettitle')
    ### end Alembic commands ###
