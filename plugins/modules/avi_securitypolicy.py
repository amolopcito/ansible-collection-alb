#!/usr/bin/python3
# module_check: supported

# Avi Version: 18.2.2
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_securitypolicy
author: Chaitanya Deshpande (@chaitanyaavi) <chaitanya.deshpande@avinetworks.com>

short_description: Module for setup of SecurityPolicy Avi RESTful Object
description:
    - This module is used to configure SecurityPolicy object
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
            - Security policy is used to specify various configuration information used to perform distributed denial of service (ddos) attacks detection and
            - mitigation.
            - Field introduced in 18.2.1.
        type: str
    dns_amplification_denyports:
        description:
            - Source ports and port ranges to deny in dns amplification attacks.
            - Field introduced in 21.1.1.
        type: dict
    dns_attacks:
        description:
            - Attacks utilizing the dns protocol operations.
            - Field introduced in 18.2.1.
        type: dict
    dns_policy_index:
        description:
            - Index of the dns policy to use for the mitigation rules applied to the dns attacks.
            - Field introduced in 18.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
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
            - The name of the security policy.
            - Field introduced in 18.2.1.
        required: true
        type: str
    network_security_policy_index:
        description:
            - Index of the network security policy to use for the mitigation rules applied to the attacks.
            - Field introduced in 18.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    oper_mode:
        description:
            - Mode of dealing with the attacks - perform detection only, or detect and mitigate the attacks.
            - Enum options - DETECTION, MITIGATION.
            - Field introduced in 18.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as DETECTION.
        type: str
    tcp_attacks:
        description:
            - Attacks utilizing the tcp protocol operations.
            - Field introduced in 18.2.1.
        type: dict
    tenant_ref:
        description:
            - Tenancy of the security policy.
            - It is a reference to an object of type tenant.
            - Field introduced in 18.2.1.
        type: str
    udp_attacks:
        description:
            - Attacks utilizing the udp protocol operations.
            - Field introduced in 18.2.1.
        type: dict
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - The uuid of the security policy.
            - Field introduced in 18.2.1.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- name: Example to create SecurityPolicy object
  vmware.alb.avi_securitypolicy:
    controller: 192.168.15.18
    username: admin
    password: something
    state: present
    name: sample_securitypolicy
"""

RETURN = '''
obj:
    description: SecurityPolicy (api/securitypolicy) object
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
        dns_amplification_denyports=dict(type='dict',),
        dns_attacks=dict(type='dict',),
        dns_policy_index=dict(type='int',),
        labels=dict(type='list',),
        markers=dict(type='list',),
        name=dict(type='str', required=True),
        network_security_policy_index=dict(type='int',),
        oper_mode=dict(type='str',),
        tcp_attacks=dict(type='dict',),
        tenant_ref=dict(type='str',),
        udp_attacks=dict(type='dict',),
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
    return avi_ansible_api(module, 'securitypolicy',
                           set())


if __name__ == '__main__':
    main()
