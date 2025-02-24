# -*- coding: utf-8 -*-

# Avi Version: 16.3.4
# Copyright 2021 VMware, Inc. All rights reserved. VMware Confidential
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)


class ModuleDocFragment(object):
    # Avi common documentation fragment
    DOCUMENTATION = r'''
options:
    controller:
        description:
            - IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).
        type: str
        default: ''
    username:
        description:
            - Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).
        type: str
        default: ''
    password:
        description:
            - Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).
        type: str
        default: ''
    tenant:
        description:
            - Name of tenant used for all Avi API calls and context of object.
        type: str
        default: admin
    tenant_uuid:
        description:
            - UUID of tenant used for all Avi API calls and context of object.
        type: str
        default: ''
    api_version:
        description:
            - Avi API version of to use for Avi API and objects.
        type: str
        default: 16.4.4
    avi_credentials:
        description:
            - Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.
        suboptions:
            controller:
                description:
                  - Avi controller IP or SQDN
                type: str
            username:
                description:
                  - Avi controller username
                type: str
            password:
                description:
                  - Avi controller password
                type: str
            api_version:
                description:
                  - Avi controller version
                type: str
                default: 16.4.4
            tenant:
                description:
                  - Avi controller tenant
                type: str
                default: admin
            tenant_uuid:
                description:
                  - Avi controller tenant UUID
                type: str
                default: ''
            port:
                description:
                  - Avi controller port
                type: int
            token:
                description:
                  - Avi controller API token
                type: str
            timeout:
                description:
                  - Avi controller request timeout
                type: int
                default: 300
            session_id:
                description:
                  - Avi controller API session id to reuse existing session with csrftoken
                type: str
            csrftoken:
                description:
                  - Avi controller API csrftoken to reuse existing session with session id
                type: str
        type: dict
    api_context:
        description:
            - Avi API context that includes current session ID and CSRF Token.
            - This allows user to perform single login and re-use the session.
        type: dict
    avi_disable_session_cache_as_fact:
        description:
            - It disables avi session information to be cached as a fact.
        type: bool
        default: false

notes:
  - For more information on using Ansible to manage Avi Network devices see U(https://www.ansible.com/ansible-avi-networks).
'''
