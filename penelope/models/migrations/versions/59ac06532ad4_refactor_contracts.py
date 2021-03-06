"""refactor contracts

Revision ID: 59ac06532ad4
Revises: 275c8091ee37
Create Date: 2013-12-17 17:16:27.437434

"""

# revision identifiers, used by Alembic.
revision = '59ac06532ad4'
down_revision = '275c8091ee37'

from alembic import op
import sqlalchemy as sa

from sqlalchemy.orm.session import Session
from penelope.models import TimeEntry


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('time_entries', sa.Column('customer_request_id', sa.String(), nullable=True))
    op.drop_column('time_entries', u'contract_id')
    op.drop_column('customer_requests', u'placement')

    context = op.get_context()
    session = Session()
    session.bind = context.bind

    for tp in session.query(TimeEntry):
        for trac in tp.project.tracs:
            cr = session.execute('select value from "trac_%s".ticket_custom where name=\'customerrequest\' and ticket=%s' % (trac.trac_name, tp.ticket)).fetchone()
            sql_cr = session.execute('select id from customer_requests where id=\'%s\'' % cr.value).fetchone()
            tp.customer_request_id = sql_cr.id
    session.commit()
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('time_entries', sa.Column(u'contract_id', sa.VARCHAR(), nullable=True))
    op.add_column('customer_requests', sa.Column(u'placement', sa.String(), nullable=True))
    op.drop_column('time_entries', 'customer_request_id')
    ### end Alembic commands ###
