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
module: avi_vsdatascriptset
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of VSDataScriptSet Avi RESTful Object
description:
    - This module is used to configure VSDataScriptSet object
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
    created_by:
        description:
            - Creator name.
            - Field introduced in 17.1.11,17.2.4.
        type: str
    datascript:
        description:
            - Datascripts to execute.
        type: list
    description:
        description:
            - User defined description for the object.
        type: str
    geo_db_ref:
        description:
            - Geo location mapping database used by this datascriptset.
            - It is a reference to an object of type geodb.
            - Field introduced in 21.1.1.
        type: str
    ip_reputation_db_ref:
        description:
            - Ip reputation database that can be used by datascript functions.
            - It is a reference to an object of type ipreputationdb.
            - Field introduced in 20.1.3.
        type: str
    ipgroup_refs:
        description:
            - Uuid of ip groups that could be referred by vsdatascriptset objects.
            - It is a reference to an object of type ipaddrgroup.
        type: list
    labels:
        description:
            - Key value pairs for granular object access control.
            - Also allows for classification and tagging of similar objects.
            - Field deprecated in 20.1.5.
            - Field introduced in 20.1.2.
            - Maximum of 4 items allowed.
        type: list
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
        type: list
    name:
        description:
            - Name for the virtual service datascript collection.
        required: true
        type: str
    pool_group_refs:
        description:
            - Uuid of pool groups that could be referred by vsdatascriptset objects.
            - It is a reference to an object of type poolgroup.
        type: list
    pool_refs:
        description:
            - Uuid of pools that could be referred by vsdatascriptset objects.
            - It is a reference to an object of type pool.
        type: list
    protocol_parser_refs:
        description:
            - List of protocol parsers that could be referred by vsdatascriptset objects.
            - It is a reference to an object of type protocolparser.
            - Field introduced in 18.2.3.
            - Allowed in basic edition, essentials edition, enterprise edition.
        type: list
    rate_limiters:
        description:
            - The rate limit definitions needed for this datascript.
            - The name is composed of the virtual service name and the datascript name.
            - Field introduced in 18.2.9.
            - Allowed in basic edition, essentials edition, enterprise edition.
        type: list
    string_group_refs:
        description:
            - Uuid of string groups that could be referred by vsdatascriptset objects.
            - It is a reference to an object of type stringgroup.
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
            - Uuid of the virtual service datascript collection.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- name: Example to create VSDataScriptSet object
  vmware.alb.avi_vsdatascriptset:
    controller: 192.168.15.18
    username: admin
    password: something
    state: present
    name: sample_vsdatascriptset
"""

RETURN = '''
obj:
    description: VSDataScriptSet (api/vsdatascriptset) object
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
        created_by=dict(type='str',),
        datascript=dict(type='list',),
        description=dict(type='str',),
        geo_db_ref=dict(type='str',),
        ip_reputation_db_ref=dict(type='str',),
        ipgroup_refs=dict(type='list',),
        labels=dict(type='list',),
        markers=dict(type='list',),
        name=dict(type='str', required=True),
        pool_group_refs=dict(type='list',),
        pool_refs=dict(type='list',),
        protocol_parser_refs=dict(type='list',),
        rate_limiters=dict(type='list',),
        string_group_refs=dict(type='list',),
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
    return avi_ansible_api(module, 'vsdatascriptset',
                           set())


if __name__ == '__main__':
    main()
