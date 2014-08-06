from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
SECS_IN_HR = 60.0*60.0
WORK_HOURS_IN_DAY = 8.0
GOOGLE_DOCS = 'google docs'
SVN = 'svn'
TRAC = 'trac'
TRAC_REPORT = 'trac report'
GENERIC_APP = 'generic'
BACKLOG_PRIORITY_ORDER = 'priority'
BACKLOG_MODIFICATION_ORDER = 'modification'


def timedelta_as_work_days(td):
    return (td.days*24.0 + td.seconds/SECS_IN_HR) / WORK_HOURS_IN_DAY


def timedelta_as_work_hours(td):
    return (td.days*24.0 + td.seconds/SECS_IN_HR)


def timedelta_as_human_str(td, seconds=False):
    """
    Formats a timedelta for human consumption. Also used by some reports.
    """
    if td is None:
        return ''
    hh, rem = divmod(td.days*24.0*SECS_IN_HR + td.seconds, SECS_IN_HR)
    mm, ss = divmod(rem, 60)
    if seconds or ss:
        return '%d:%02d:%02d' % (hh, mm, ss)
    else:
        return '%d:%02d' % (hh, mm)


class classproperty(object):
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner):
        if instance:
            return self.getter(instance)
        else:
            return self.getter(owner)


from penelope.models.dashboard import Project; Project
from penelope.models.dashboard import User; User
from penelope.models.dashboard import GlobalConfig; GlobalConfig
from penelope.models.dashboard import Role; Role
from penelope.models.dashboard import OpenId; OpenId
from penelope.models.dashboard import PasswordResetToken; PasswordResetToken
from penelope.models.dashboard import Application; Application
from penelope.models.dashboard import ApplicationACL; ApplicationACL
from penelope.models.dashboard import KanbanACL; KanbanACL
from penelope.models.dashboard import CustomerRequest; CustomerRequest
from penelope.models.dashboard import Estimation; Estimation
from penelope.models.dashboard import Group; Group
from penelope.models.dashboard import SavedQuery; SavedQuery
from penelope.models.dashboard import Customer; Customer
from penelope.models.dashboard import Contract; Contract
from penelope.models.dashboard import KanbanBoard; KanbanBoard
from penelope.models.dashboard import Cost; Cost
from penelope.models.dashboard import Activity; Activity
from penelope.models.dashboard import Principal; Principal
from penelope.models.dashboard import GenericApp; GenericApp
from penelope.models.dashboard import Trac; Trac
from penelope.models.dashboard import TracReport; TracReport
from penelope.models.dashboard import Subversion; Subversion
from penelope.models.dashboard import GoogleDoc; GoogleDoc
from penelope.models.dashboard import modify_application_type; modify_application_type
from penelope.models.tp import TimeEntry; TimeEntry
from penelope.models.workflow import Workflow; Workflow
from penelope.models.dublincore import DublinCore; DublinCore
from penelope.models.tickets import ticket_store; ticket_store
from penelope.models.tickets import TicketStore; TicketStore
