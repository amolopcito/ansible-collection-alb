#!/usr/bin/python3
# module_check: supported

# Avi Version: 17.1.1
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_stringgroup
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of StringGroup Avi RESTful Object
description:
    - This module is used to configure StringGroup object
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
            - User defined description for the object.
        type: str
    kv:
        description:
            - Configure key value in the string group.
        type: list
    labels:
        description:
            - Key value pairs for granular object access control.
            - Also allows for classification and tagging of similar objects.
            - Field deprecated in 20.1.5.
            - Field introduced in 20.1.2.
            - Maximum of 4 items allowed.
        type: list
    longest_match:
        description:
            - Enable the longest match, default is the shortest match.
            - Field introduced in 18.2.8.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
        type: list
    name:
        description:
            - Name of the string group.
        required: true
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
        type: str
    type:
        description:
            - Type of stringgroup.
            - Enum options - SG_TYPE_STRING, SG_TYPE_KEYVAL.
            - Default value when not specified in API or module is interpreted by Avi Controller as SG_TYPE_STRING.
        required: true
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the string group.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
  - name: Create a string group configuration
    vmware.alb.avi_stringgroup:
      controller: '{{ controller }}'
      password: '{{ password }}'
      username: '{{ username }}'
      kv:
      - key: text/html
      - key: text/xml
      - key: text/plain
      - key: text/css
      - key: text/javascript
      - key: application/javascript
      - key: application/x-javascript
      - key: application/xml
      - key: application/pdf
      name: System-Compressible-Content-Types
      tenant_ref: /api/tenant?name=admin
      type: SG_TYPE_STRING
"""

RETURN = '''
obj:
    description: StringGroup (api/stringgroup) object
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
        kv=dict(type='list',),
        labels=dict(type='list',),
        longest_match=dict(type='bool',),
        markers=dict(type='list',),
        name=dict(type='str', required=True),
        tenant_ref=dict(type='str',),
        type=dict(type='str', required=True),
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
    return avi_ansible_api(module, 'stringgroup',
                           set())


if __name__ == '__main__':
    main()
