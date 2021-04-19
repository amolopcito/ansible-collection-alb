#!/usr/bin/python3
# module_check: supported

# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_controllersite
author: Chaitanya Deshpande (@chaitanyaavi) <chaitanya.deshpande@avinetworks.com>

short_description: Module for setup of ControllerSite Avi RESTful Object
description:
    - This module is used to configure ControllerSite object
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
        choices: ["add", "replace", "delete"]
        type: str
    address:
        description:
            - Ip address or a dns resolvable, fully qualified domain name of the site controller cluster.
            - Field introduced in 18.2.5.
        required: true
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
        type: dict
    name:
        description:
            - Name for the site controller cluster.
            - Field introduced in 18.2.5.
        required: true
        type: str
    port:
        description:
            - The controller site cluster's rest api port number.
            - Allowed values are 1-65535.
            - Field introduced in 18.2.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as 443.
        type: int
    tenant_ref:
        description:
            - Reference for the tenant.
            - It is a reference to an object of type tenant.
            - Field introduced in 18.2.5.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Reference for the site controller cluster.
            - Field introduced in 18.2.5.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- name: Example to create ControllerSite object
  vmware.alb.avi_controllersite:
    controller: 192.168.15.18
    username: admin
    password: something
    state: present
    name: sample_controllersite
"""

RETURN = '''
obj:
    description: ControllerSite (api/controllersite) object
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
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete']),
        address=dict(type='str', required=True),
        configpb_attributes=dict(type='dict',),
        name=dict(type='str', required=True),
        port=dict(type='int',),
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
    return avi_ansible_api(module, 'controllersite',
                           set())


if __name__ == '__main__':
    main()
