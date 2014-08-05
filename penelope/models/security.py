from pyramid.security import ALL_PERMISSIONS
from pyramid.security import Allow, Deny
from pyramid.security import Authenticated


class ACL(list):
    """ Named ACL map

    ACL contains list of permit rules, for example::

      >> acl = ACL('test', 'Test ACL')
      >> acl.allow('system.Everyone', 'View')
      >> acl.deny('system.Everyone', 'Edit')

      >> list(acl)
      [(Allow, 'system.Everyone', ('View',)),
       (Deny, 'system.Everyone', ('Edit',))]

    """

    def __init__(self, name):
        self.name = name

    def get(self, typ, role):
        for r in self:
            if r[0] == typ and r[1] == role:
                return r

        return None

    def allow(self, role, *permissions):
        """ Give permissions to role """

        if not isinstance(role, basestring):
            role = role.id

        rec = self.get(Allow, role)
        if rec is None:
            rec = [Allow, role, set()]
            self.append(rec)

        if rec[2] is ALL_PERMISSIONS:
            return

        if ALL_PERMISSIONS in permissions:
            rec[2] = ALL_PERMISSIONS
        else:
            rec[2].update(permissions)

    def deny(self, role, *permissions):
        """ Deny permissions for role """

        if not isinstance(role, basestring):
            role = role.id

        rec = self.get(Deny, role)
        if rec is None:
            rec = [Deny, role, set()]
            self.append(rec)

        if rec[2] is ALL_PERMISSIONS:
            return

        if ALL_PERMISSIONS in permissions:
            rec[2] = ALL_PERMISSIONS
        else:
            rec[2].update(permissions)

    def unset(self, role, *permissions):
        """ Unset any previously defined permissions """
        for perm in permissions:
            for rec in self:
                if role is not None and rec[1] != role:
                    continue

                if rec[2] is ALL_PERMISSIONS or perm is ALL_PERMISSIONS:
                    rec[2] = set()
                else:
                    if perm in rec[2]:
                        rec[2].remove(perm)

        records = []
        for rec in self:
            if rec[2]:
                records.append(rec)
        self[:] = records


DEFAULT_ACL = ACL('default_por_acl') 
DEFAULT_ACL.allow('system.Everyone', 'view_anon')
DEFAULT_ACL.allow('role:administrator', ALL_PERMISSIONS)

#/home
DEFAULT_ACL.allow(Authenticated, 'view_home')
DEFAULT_ACL.allow('role:redturtle_developer', 'search')

#/manage_svn
DEFAULT_ACL.allow('role:redturtle_developer', 'manage_svn')

#/view_iterations
DEFAULT_ACL.allow('role:local_developer', 'view_iterations')
DEFAULT_ACL.allow('role:local_project_manager', 'view_iterations')
DEFAULT_ACL.allow('role:internal_developer', 'view_iterations')
DEFAULT_ACL.allow('role:secretary', 'view_iterations')
DEFAULT_ACL.allow('role:project_manager', 'view_iterations')

#/manage_iterations and /generate_iterations
DEFAULT_ACL.allow('role:local_project_manager', 'manage_iterations')
DEFAULT_ACL.allow('role:secretary', 'manage_iterations')
DEFAULT_ACL.allow('role:project_manager', 'manage_iterations')

#/add_entry
DEFAULT_ACL.allow('role:local_developer', 'add_entry')
DEFAULT_ACL.allow('role:local_project_manager', 'add_entry')
DEFAULT_ACL.allow('role:external_developer', 'add_entry')
DEFAULT_ACL.allow('role:internal_developer', 'add_entry')
DEFAULT_ACL.allow('role:secretary', 'add_entry')
DEFAULT_ACL.allow('role:project_manager', 'add_entry')

#/reports/index
DEFAULT_ACL.allow('role:local_project_manager', 'reports_index')
DEFAULT_ACL.allow('role:local_developer', 'reports_index')
DEFAULT_ACL.allow('role:secretary', 'reports_index')
DEFAULT_ACL.allow('role:project_manager', 'reports_index')

#/reports/report_custom
DEFAULT_ACL.allow('role:local_project_manager', 'reports_custom')
DEFAULT_ACL.allow('role:secretary', 'reports_custom')
DEFAULT_ACL.allow('role:project_manager', 'reports_custom')

#/reports/report_all_entries
DEFAULT_ACL.allow('role:local_project_manager', 'reports_all_entries')
DEFAULT_ACL.allow('role:local_developer', 'reports_all_entries')
DEFAULT_ACL.allow('role:secretary', 'reports_all_entries')
DEFAULT_ACL.allow('role:project_manager', 'reports_all_entries')

#/reports/report_state_change
DEFAULT_ACL.allow('role:secretary', 'reports_state_change')
DEFAULT_ACL.allow('role:project_manager', 'reports_state_change')
DEFAULT_ACL.allow('role:local_project_manager', 'reports_state_change')

#/reports/my_entries
DEFAULT_ACL.allow('role:local_developer', 'reports_my_entries')
DEFAULT_ACL.allow('role:local_project_manager', 'reports_my_entries')
DEFAULT_ACL.allow('role:internal_developer', 'reports_my_entries')
DEFAULT_ACL.allow('role:external_developer', 'reports_my_entries')
DEFAULT_ACL.allow('role:secretary', 'reports_my_entries')
DEFAULT_ACL.allow('role:project_manager', 'reports_my_entries')

#/backlog
DEFAULT_ACL.allow('role:local_developer', 'view_backlog')
DEFAULT_ACL.allow('role:local_project_manager', 'view_backlog')
DEFAULT_ACL.allow('role:secretary', 'view_backlog')

CRUD_ACL = ACL('por_crud_acl')
CRUD_ACL.allow('role:administrator', ALL_PERMISSIONS)
CRUD_ACL.allow('role:redturtle_developer', 'search')

#Customer
CRUD_ACL.allow(Authenticated, 'customer_listing')
