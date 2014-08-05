from sqlalchemy import Column, Unicode
from repoze.workflow import get_workflow


class Workflow(object):
    """
    Workflow enable implementation for POR project
    """
    workflow_state = Column(Unicode)

    def __init__(self, *args, **kwargs):
        super(Workflow, self).__init__(*args, **kwargs)
        wf = get_workflow(self, self.__class__.__name__)
        if wf:
            wf.initialize(self)
