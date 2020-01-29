#!/usr/bin/env python3

"""

Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.


"""
__author__ = "Bryan Byrne <brybyrne@cisco.com>"
__contributors__ = ["Dmitry Figol <git@dmfigol.me>"]
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

from ncclient import manager
import xmltodict

import constants
import utils

FILTER = """
<filter>
  <access-lists xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-acl-oper">
    <access-list>
      <access-control-list-name>CISCO_LIVE_IN</access-control-list-name>
    </access-list>
  </access-lists>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <ip>
      <access-list>
        <extended xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-acl"/>
      </access-list>
    </ip>
  </native>
</filter>
"""


def main():
    with manager.connect(**constants.NC_CONN_PARAMS) as m:
        nc_reply = m.get(FILTER)
        print(utils.prettify_xml(nc_reply.xml))

        acl_data = xmltodict.parse(nc_reply.xml)["rpc-reply"]["data"]
        acl_conf = acl_data["native"]["ip"]["access-list"]["extended"]["access-list-seq-rule"]
        acl_name = acl_data["access-lists"]["access-list"]
        acl_match = acl_data["access-lists"]["access-list"]["access-list-entries"]["access-list-entry"]

        # Process the xml data into a readable format.
        print("Access-List Name: {}".format(acl_name["access-control-list-name"]["#text"]))
        for ace in acl_conf:
            try:
                print(" For ACE: {}".format(ace["sequence"]))
                print("  Protocol: {}".format(ace["ace-rule"]["protocol"]))
                host_ip = ace["ace-rule"]["ipv4-address"]
                print("   Host IP: {}".format(host_ip))
                print("   Wildcard Mask: {}".format(ace["ace-rule"]["mask"]))
                print("   Action: {}".format(ace["ace-rule"]["action"]))
            except KeyError:
                print("   Action: {}".format(ace["ace-rule"]["action"]))
            except Exception:
                print("  Cannot Understand ACE")

        for rule in acl_match:
            print(
              f"For SEQ number: {rule['rule-name']} the number of ACE"
              f"matches is: {rule['access-list-entries-oper-data']['match-counter']}"
            )


if __name__ == '__main__':
    main()
