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
__author__ = "Dmitry Figol <git@dmfigol.me>"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

from ncclient import manager
import xmltodict

import constants
import utils

CONFIG = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <vrf>
            <definition>
                <name>Mgmt-vrf</name>
                <address-family>
                    <ipv4/>
                    <ipv6/>
                </address-family>
            </definition>
            <definition>
                <name>Cisco-LIVE</name>
                <address-family>
                    <ipv4/>
                    <ipv6/>
                </address-family>
            </definition>
        </vrf>
    </native>
</config>
"""


def main():
    with manager.connect(**constants.NC_CONN_PARAMS) as m:
        nc_reply = m.edit_config(CONFIG, target="running")


if __name__ == '__main__':
    main()
