#!/usr/bin/python3
# module_check: supported

# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_alertsyslogconfig
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of AlertSyslogConfig Avi RESTful Object
description:
    - This module is used to configure AlertSyslogConfig object
    - more examples at U(https://github.com/avinetworks/devops)
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    avi_api_update_method:
        description:
            - Default method for object update is HTTP PUT.
            - Setting to patch will override that behavior to use HTTP PATCH.
        default: put
        choices: ["put", "patch"]
        type: str
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        choices: ["add", "replace", "delete", "remove"]
        type: str
    avi_patch_path:
        description:
            - Patch path to use when using avi_api_update_method as patch.
        type: str
    avi_patch_value:
        description:
            - Patch value to use when using avi_api_update_method as patch.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
        type: dict
    description:
        description:
            - User defined description for alert syslog config.
        type: str
    name:
        description:
            - A user-friendly name of the syslog notification.
        required: true
        type: str
    syslog_servers:
        description:
            - The list of syslog servers.
        type: list
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Unique object identifier of the object.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
  - name: Create Alert Syslog object to forward all events to external syslog server
    vmware.alb.avi_alertsyslogconfig:
      controller: '{{ controller }}'
      name: Roberts-syslog
      password: '{{ password }}'
      syslog_servers:
      - syslog_server: 192.168.15.11
        syslog_server_port: 514
        udp: true
      tenant_ref: /api/tenant?name=admin
      username: '{{ username }}'
"""

RETURN = '''
obj:
    description: AlertSyslogConfig (api/alertsyslogconfig) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, avi_ansible_api)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete', 'remove']),
        avi_patch_path=dict(type='str',),
        avi_patch_value=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        name=dict(type='str', required=True),
        syslog_servers=dict(type='list',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'alertsyslogconfig',
                           set())


if __name__ == '__main__':
    main()
