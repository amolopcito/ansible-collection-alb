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
module: avi_gslbservice
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of GslbService Avi RESTful Object
description:
    - This module is used to configure GslbService object
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
    application_persistence_profile_ref:
        description:
            - The federated application persistence associated with gslbservice site persistence functionality.
            - It is a reference to an object of type applicationpersistenceprofile.
            - Field introduced in 17.2.1.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
        type: dict
    controller_health_status_enabled:
        description:
            - Gs member's overall health status is derived based on a combination of controller and datapath health-status inputs.
            - Note that the datapath status is determined by the association of health monitor profiles.
            - Only the controller provided status is determined through this configuration.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    created_by:
        description:
            - Creator name.
            - Field introduced in 17.1.2.
        type: str
    description:
        description:
            - User defined description for the object.
        type: str
    domain_names:
        description:
            - Fully qualified domain name of the gslb service.
            - Minimum of 1 items required.
        required: true
        type: list
    down_response:
        description:
            - Response to the client query when the gslb service is down.
        type: dict
    enabled:
        description:
            - Enable or disable the gslb service.
            - If the gslb service is enabled, then the vips are sent in the dns responses based on reachability and configured algorithm.
            - If the gslb service is disabled, then the vips are no longer available in the dns response.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    groups:
        description:
            - Select list of pools belonging to this gslb service.
            - Minimum of 1 items required.
        required: true
        type: list
    health_monitor_refs:
        description:
            - Verify vs health by applying one or more health monitors.
            - Active monitors generate synthetic traffic from dns service engine and to mark a vs up or down based on the response.
            - It is a reference to an object of type healthmonitor.
            - Maximum of 6 items allowed.
        type: list
    health_monitor_scope:
        description:
            - Health monitor probe can be executed for all the members or it can be executed only for third-party members.
            - This operational mode is useful to reduce the number of health monitor probes in case of a hybrid scenario.
            - In such a case, avi members can have controller derived status while non-avi members can be probed by via health monitor probes in dataplane.
            - Enum options - GSLB_SERVICE_HEALTH_MONITOR_ALL_MEMBERS, GSLB_SERVICE_HEALTH_MONITOR_ONLY_NON_AVI_MEMBERS.
            - Default value when not specified in API or module is interpreted by Avi Controller as GSLB_SERVICE_HEALTH_MONITOR_ALL_MEMBERS.
        type: str
    hm_off:
        description:
            - This field is an internal field and is used in se.
            - Field introduced in 18.2.2.
        type: bool
    is_federated:
        description:
            - This field indicates that this object is replicated across gslb federation.
            - Field introduced in 17.1.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
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
    min_members:
        description:
            - The minimum number of members to distribute traffic to.
            - Allowed values are 1-65535.
            - Special values are 0 - 'disable'.
            - Field introduced in 17.2.4.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    name:
        description:
            - Name for the gslb service.
        required: true
        type: str
    num_dns_ip:
        description:
            - Number of ip addresses of this gslb service to be returned by the dns service.
            - Enter 0 to return all ip addresses.
            - Allowed values are 1-20.
            - Special values are 0- 'return all ip addresses'.
        type: int
    pool_algorithm:
        description:
            - The load balancing algorithm will pick a gslb pool within the gslb service list of available pools.
            - Enum options - GSLB_SERVICE_ALGORITHM_PRIORITY, GSLB_SERVICE_ALGORITHM_GEO.
            - Field introduced in 17.2.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as GSLB_SERVICE_ALGORITHM_PRIORITY.
        type: str
    resolve_cname:
        description:
            - This field indicates that for a cname query, respond with resolved cnames in the additional section with a records.
            - Field introduced in 18.2.5.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    site_persistence_enabled:
        description:
            - Enable site-persistence for the gslbservice.
            - Field introduced in 17.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
        type: str
    ttl:
        description:
            - Ttl value (in seconds) for records served for this gslb service by the dns service.
            - Allowed values are 0-86400.
            - Unit is sec.
        type: int
    url:
        description:
            - Avi controller URL of the object.
        type: str
    use_edns_client_subnet:
        description:
            - Use the client ip subnet from the edns option as source ipaddress for client geo-location and consistent hash algorithm.
            - Default is true.
            - Field introduced in 17.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    uuid:
        description:
            - Uuid of the gslb service.
        type: str
    wildcard_match:
        description:
            - Enable wild-card match of fqdn  if an exact match is not found in the dns table, the longest match is chosen by wild-carding the fqdn in the dns
            - request.
            - Default is false.
            - Field introduced in 17.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- name: Example to create GslbService object
  vmware.alb.avi_gslbservice:
    controller: 192.168.15.18
    username: admin
    password: something
    state: present
    name: sample_gslbservice
"""

RETURN = '''
obj:
    description: GslbService (api/gslbservice) object
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
        application_persistence_profile_ref=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        controller_health_status_enabled=dict(type='bool',),
        created_by=dict(type='str',),
        description=dict(type='str',),
        domain_names=dict(type='list', required=True),
        down_response=dict(type='dict',),
        enabled=dict(type='bool',),
        groups=dict(type='list', required=True),
        health_monitor_refs=dict(type='list',),
        health_monitor_scope=dict(type='str',),
        hm_off=dict(type='bool',),
        is_federated=dict(type='bool',),
        labels=dict(type='list',),
        markers=dict(type='list',),
        min_members=dict(type='int',),
        name=dict(type='str', required=True),
        num_dns_ip=dict(type='int',),
        pool_algorithm=dict(type='str',),
        resolve_cname=dict(type='bool',),
        site_persistence_enabled=dict(type='bool',),
        tenant_ref=dict(type='str',),
        ttl=dict(type='int',),
        url=dict(type='str',),
        use_edns_client_subnet=dict(type='bool',),
        uuid=dict(type='str',),
        wildcard_match=dict(type='bool',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'gslbservice',
                           set())


if __name__ == '__main__':
    main()
