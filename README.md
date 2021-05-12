# VMware Advanced Load Balancer (formerly Avi) Ansible Collection 

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10**.

<!--end requires_ansible-->

## Installation and Usage

Ansible must be installed
```
pip install ansible
```

Install ALB collection using `ansible-galaxy` CLI:
```
ansible-galaxy collection install amolopcito.alb
```

Install ALB collection using `requirements.yml` file:

Create `requirements.yml` file using below contents
```yaml
collections:
- name: amolopcito.alb
```

Install the collection:
```
ansible-galaxy collection install -r requirements.yml
```

### Required Python libraries

ALB collection depends upon following third party libraries:

* requests

### Installing required libraries

After ALB collection installation we need to install the required python libraries using following command:
```
pip install requests
```

### Modules
Name | Description
--- | ---
[amolopcito.alb.avi_labelgroup](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_labelgroup.rst)|Module to create update or delete LabelGroup
[amolopcito.alb.avi_albservicesconfig](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_albservicesconfig.rst)|Module to create update or delete ALBServicesConfig
[amolopcito.alb.avi_systemlimits](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_systemlimits.rst)|Module to create update or delete SystemLimits
[amolopcito.alb.avi_licenseledgerdetails](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_licenseledgerdetails.rst)|Module to create update or delete LicenseLedgerDetails
[amolopcito.alb.avi_controllerproperties](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_controllerproperties.rst)|Module to create update or delete ControllerProperties
[amolopcito.alb.avi_useraccountprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_useraccountprofile.rst)|Module to create update or delete UserAccountProfile
[amolopcito.alb.avi_cloudproperties](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_cloudproperties.rst)|Module to create update or delete CloudProperties
[amolopcito.alb.avi_seproperties](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_seproperties.rst)|Module to create update or delete SeProperties
[amolopcito.alb.avi_tenant](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_tenant.rst)|Module to create update or delete Tenant
[amolopcito.alb.avi_cloudconnectoruser](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_cloudconnectoruser.rst)|Module to create update or delete CloudConnectorUser
[amolopcito.alb.avi_hardwaresecuritymodulegroup](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_hardwaresecuritymodulegroup.rst)|Module to create update or delete HardwareSecurityModuleGroup
[amolopcito.alb.avi_alertscriptconfig](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_alertscriptconfig.rst)|Module to create update or delete AlertScriptConfig
[amolopcito.alb.avi_customipamdnsprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_customipamdnsprofile.rst)|Module to create update or delete CustomIpamDnsProfile
[amolopcito.alb.avi_networkprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_networkprofile.rst)|Module to create update or delete NetworkProfile
[amolopcito.alb.avi_stringgroup](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_stringgroup.rst)|Module to create update or delete StringGroup
[amolopcito.alb.avi_ipaddrgroup](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_ipaddrgroup.rst)|Module to create update or delete IpAddrGroup
[amolopcito.alb.avi_pkiprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_pkiprofile.rst)|Module to create update or delete PKIProfile
[amolopcito.alb.avi_sslprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_sslprofile.rst)|Module to create update or delete SSLProfile
[amolopcito.alb.avi_applicationpersistenceprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_applicationpersistenceprofile.rst)|Module to create update or delete ApplicationPersistenceProfile
[amolopcito.alb.avi_alertemailconfig](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_alertemailconfig.rst)|Module to create update or delete AlertEmailConfig
[amolopcito.alb.avi_snmptrapprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_snmptrapprofile.rst)|Module to create update or delete SnmpTrapProfile
[amolopcito.alb.avi_autoscalelaunchconfig](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_autoscalelaunchconfig.rst)|Module to create update or delete AutoScaleLaunchConfig
[amolopcito.alb.avi_fileobject](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_fileobject.rst)|Module to create update or delete FileObject
[amolopcito.alb.avi_securitypolicy](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_securitypolicy.rst)|Module to create update or delete SecurityPolicy
[amolopcito.alb.avi_protocolparser](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_protocolparser.rst)|Module to create update or delete ProtocolParser
[amolopcito.alb.avi_jwtserverprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_jwtserverprofile.rst)|Module to create update or delete JWTServerProfile
[amolopcito.alb.avi_wafprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_wafprofile.rst)|Module to create update or delete WafProfile
[amolopcito.alb.avi_wafapplicationsignatureprovider](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_wafapplicationsignatureprovider.rst)|Module to create update or delete WafApplicationSignatureProvider
[amolopcito.alb.avi_errorpagebody](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_errorpagebody.rst)|Module to create update or delete ErrorPageBody
[amolopcito.alb.avi_testsedatastorelevel3](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_testsedatastorelevel3.rst)|Module to create update or delete TestSeDatastoreLevel3
[amolopcito.alb.avi_botconfigconsolidator](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_botconfigconsolidator.rst)|Module to create update or delete BotConfigConsolidator
[amolopcito.alb.avi_federationcheckpoint](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_federationcheckpoint.rst)|Module to create update or delete FederationCheckpoint
[amolopcito.alb.avi_gslbgeodbprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_gslbgeodbprofile.rst)|Module to create update or delete GslbGeoDbProfile
[amolopcito.alb.avi_siteversion](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_siteversion.rst)|Module to create update or delete SiteVersion
[amolopcito.alb.avi_image](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_image.rst)|Module to create update or delete Image
[amolopcito.alb.avi_controllerportalregistration](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_controllerportalregistration.rst)|Module to create update or delete ControllerPortalRegistration
[amolopcito.alb.avi_dynamicdnsrecord](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_dynamicdnsrecord.rst)|Module to create update or delete DynamicDnsRecord
[amolopcito.alb.avi_controllersite](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_controllersite.rst)|Module to create update or delete ControllerSite
[amolopcito.alb.avi_role](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_role.rst)|Module to create update or delete Role
[amolopcito.alb.avi_albservicesfileupload](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_albservicesfileupload.rst)|Module to create update or delete ALBServicesFileUpload
[amolopcito.alb.avi_webhook](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_webhook.rst)|Module to create update or delete Webhook
[amolopcito.alb.avi_securitymanagerdata](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_securitymanagerdata.rst)|Module to create update or delete SecurityManagerData
[amolopcito.alb.avi_cluster](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_cluster.rst)|Module to create update or delete Cluster
[amolopcito.alb.avi_poolgroupdeploymentpolicy](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_poolgroupdeploymentpolicy.rst)|Module to create update or delete PoolGroupDeploymentPolicy
[amolopcito.alb.avi_jwtprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_jwtprofile.rst)|Module to create update or delete JWTProfile
[amolopcito.alb.avi_backupconfiguration](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_backupconfiguration.rst)|Module to create update or delete BackupConfiguration
[amolopcito.alb.avi_clusterclouddetails](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_clusterclouddetails.rst)|Module to create update or delete ClusterCloudDetails
[amolopcito.alb.avi_certificatemanagementprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_certificatemanagementprofile.rst)|Module to create update or delete CertificateManagementProfile
[amolopcito.alb.avi_ipamdnsproviderprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_ipamdnsproviderprofile.rst)|Module to create update or delete IpamDnsProviderProfile
[amolopcito.alb.avi_analyticsprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_analyticsprofile.rst)|Module to create update or delete AnalyticsProfile
[amolopcito.alb.avi_wafpolicypsmgroup](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_wafpolicypsmgroup.rst)|Module to create update or delete WafPolicyPSMGroup
[amolopcito.alb.avi_botmapping](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_botmapping.rst)|Module to create update or delete BotMapping
[amolopcito.alb.avi_natpolicy](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_natpolicy.rst)|Module to create update or delete NatPolicy
[amolopcito.alb.avi_applicationprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_applicationprofile.rst)|Module to create update or delete ApplicationProfile
[amolopcito.alb.avi_microservicegroup](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_microservicegroup.rst)|Module to create update or delete MicroServiceGroup
[amolopcito.alb.avi_ipreputationdb](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_ipreputationdb.rst)|Module to create update or delete IPReputationDB
[amolopcito.alb.avi_geodb](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_geodb.rst)|Module to create update or delete GeoDB
[amolopcito.alb.avi_errorpageprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_errorpageprofile.rst)|Module to create update or delete ErrorPageProfile
[amolopcito.alb.avi_testsedatastorelevel2](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_testsedatastorelevel2.rst)|Module to create update or delete TestSeDatastoreLevel2
[amolopcito.alb.avi_gslb](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_gslb.rst)|Module to create update or delete Gslb
[amolopcito.alb.avi_upgradestatusinfo](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_upgradestatusinfo.rst)|Module to create update or delete UpgradeStatusInfo
[amolopcito.alb.avi_upgradestatussummary](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_upgradestatussummary.rst)|Module to create update or delete UpgradeStatusSummary
[amolopcito.alb.avi_scheduler](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_scheduler.rst)|Module to create update or delete Scheduler
[amolopcito.alb.avi_sslkeyandcertificate](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_sslkeyandcertificate.rst)|Module to create update or delete SSLKeyAndCertificate
[amolopcito.alb.avi_networksecuritypolicy](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_networksecuritypolicy.rst)|Module to create update or delete NetworkSecurityPolicy
[amolopcito.alb.avi_botdetectionpolicy](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_botdetectionpolicy.rst)|Module to create update or delete BotDetectionPolicy
[amolopcito.alb.avi_testsedatastorelevel1](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_testsedatastorelevel1.rst)|Module to create update or delete TestSeDatastoreLevel1
[amolopcito.alb.avi_backup](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_backup.rst)|Module to create update or delete Backup
[amolopcito.alb.avi_cloud](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_cloud.rst)|Module to create update or delete Cloud
[amolopcito.alb.avi_healthmonitor](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_healthmonitor.rst)|Module to create update or delete HealthMonitor
[amolopcito.alb.avi_alertsyslogconfig](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_alertsyslogconfig.rst)|Module to create update or delete AlertSyslogConfig
[amolopcito.alb.avi_vrfcontext](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_vrfcontext.rst)|Module to create update or delete VrfContext
[amolopcito.alb.avi_vcenterserver](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_vcenterserver.rst)|Module to create update or delete VCenterServer
[amolopcito.alb.avi_prioritylabels](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_prioritylabels.rst)|Module to create update or delete PriorityLabels
[amolopcito.alb.avi_nsxtsegmentruntime](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_nsxtsegmentruntime.rst)|Module to create update or delete NsxtSegmentRuntime
[amolopcito.alb.avi_gslbservice](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_gslbservice.rst)|Module to create update or delete GslbService
[amolopcito.alb.avi_actiongroupconfig](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_actiongroupconfig.rst)|Module to create update or delete ActionGroupConfig
[amolopcito.alb.avi_availabilityzone](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_availabilityzone.rst)|Module to create update or delete AvailabilityZone
[amolopcito.alb.avi_alertconfig](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_alertconfig.rst)|Module to create update or delete AlertConfig
[amolopcito.alb.avi_serverautoscalepolicy](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_serverautoscalepolicy.rst)|Module to create update or delete ServerAutoScalePolicy
[amolopcito.alb.avi_network](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_network.rst)|Module to create update or delete Network
[amolopcito.alb.avi_serviceenginegroup](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_serviceenginegroup.rst)|Module to create update or delete ServiceEngineGroup
[amolopcito.alb.avi_pool](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_pool.rst)|Module to create update or delete Pool
[amolopcito.alb.avi_trafficcloneprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_trafficcloneprofile.rst)|Module to create update or delete TrafficCloneProfile
[amolopcito.alb.avi_vsvip](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_vsvip.rst)|Module to create update or delete VsVip
[amolopcito.alb.avi_serviceengine](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_serviceengine.rst)|Module to create update or delete ServiceEngine
[amolopcito.alb.avi_networkservice](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_networkservice.rst)|Module to create update or delete NetworkService
[amolopcito.alb.avi_poolgroup](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_poolgroup.rst)|Module to create update or delete PoolGroup
[amolopcito.alb.avi_pingaccessagent](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_pingaccessagent.rst)|Module to create update or delete PingAccessAgent
[amolopcito.alb.avi_httppolicyset](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_httppolicyset.rst)|Module to create update or delete HTTPPolicySet
[amolopcito.alb.avi_dnspolicy](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_dnspolicy.rst)|Module to create update or delete DnsPolicy
[amolopcito.alb.avi_vsdatascriptset](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_vsdatascriptset.rst)|Module to create update or delete VSDataScriptSet
[amolopcito.alb.avi_l4policyset](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_l4policyset.rst)|Module to create update or delete L4PolicySet
[amolopcito.alb.avi_icapprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_icapprofile.rst)|Module to create update or delete IcapProfile
[amolopcito.alb.avi_authprofile](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_authprofile.rst)|Module to create update or delete AuthProfile
[amolopcito.alb.avi_ssopolicy](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_ssopolicy.rst)|Module to create update or delete SSOPolicy
[amolopcito.alb.avi_systemconfiguration](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_systemconfiguration.rst)|Module to create update or delete SystemConfiguration
[amolopcito.alb.avi_virtualservice](https://github.com/amolopcito/ansible-collection-alb/blob/main/docs/avi_virtualservice.rst)|Module to create update or delete VirtualService
<!--end collection content-->

### Testing with `ansible-test`

Refer [testing](testing.md) for more information.

## Publishing New Version

Examples
--------

    - hosts: localhost
      connection: local
      collections:
        - amolopcito.alb
      tasks:
        - name: Example to create create Pool object
          avi_pool:
            controller: "192.168.15.18"
            username: "admin"
            password: "password"
            name: app1-pool
            lb_algorithm: LB_ALGORITHM_LEAST_LOAD
            servers:
            - ip:
                 addr: "192.168.12.15"
                 type: 'V4'

Example using config role:
```
# config.yml
avi_config:
  pool:
    - name: role1-pool
      lb_algorithm: LB_ALGORITHM_LEAST_LOAD
      servers:
        - ip:
             addr: 192.160.1.10
             type: 'V4'
```
```
# creds.yml
avi_credentials:
    controller: "192.168.1.11"
    username: "admin"
    password: "password"
    api_version: 20.1.5
```
```
# collection.yml
---
- hosts: localhost
  connection: local
  collections:
    - amolopcito.alb
  tasks:
    - name: Create pool using aviconfig role
      import_role:
        name: aviconfig
      vars:
          avi_config_file: "config.yml"
          avi_creds_file: "creds.yml"