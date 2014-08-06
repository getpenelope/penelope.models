"""manual_fix

Revision ID: 38914e68d30f
Revises: 59ac06532ad4
Create Date: 2013-12-20 09:46:34.439525

"""

# revision identifiers, used by Alembic.
revision = '38914e68d30f'
down_revision = '59ac06532ad4'

from alembic import op
from sqlalchemy.orm.session import Session
from penelope.models import TimeEntry

def upgrade():
    context = op.get_context()
    session = Session()
    session.bind = context.bind
    for tp in session.query(TimeEntry).filter_by(customer_request_id=None):
        for trac in tp.project.tracs:
            cr = session.execute('select value from "trac_%s".ticket_custom where name=\'customerrequest\' and ticket=%s' % (trac.trac_name, tp.ticket)).fetchone()
            sql_cr = session.execute('select id from customer_requests where id=\'%s\'' % cr.value).fetchone()
            tp.customer_request_id = sql_cr.id
            print sql_cr.id
    session.commit()

def downgrade():
    pass
