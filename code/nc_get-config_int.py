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
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet2</name>
        </interface>
    </interfaces>
</filter>
"""


def main():
    with manager.connect(**constants.NC_CONN_PARAMS) as m:
        nc_reply = m.get_config('running', FILTER)
        print(utils.prettify_xml(nc_reply.xml))

        data = xmltodict.parse(nc_reply.xml, force_list="interface")["rpc-reply"]["data"]

        if "interfaces" in data:
            for intf_config in data["interfaces"]["interface"]:
                print("*" * 50)
                int_name = intf_config['name']
                if not isinstance(int_name, str):
                    int_name = int_name["#text"]
                interface_str = (
                    f"Interface: {int_name}\n"
                    f" description: {intf_config.get('description', '')}\n"
                    f" type: {intf_config['type']['#text']}\n"
                    f" enabled: {intf_config['enabled']}"
                )
                print(interface_str)
                print("*" * 50)


if __name__ == '__main__':
    main()
