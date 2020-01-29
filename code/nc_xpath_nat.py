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
import time

import constants


def main():
    time.sleep(5)
    for i in range(5):
        # Create a NETCONF session to the router with ncclient
        with manager.connect(**constants.NC_CONN_PARAMS) as m:
            nc_reply = m.get(filter=('xpath', "access-lists/access-list/access-list-entries/access-list-entry[rule-name='20']/access-list-entries-oper-data/match-counter"))
            acl_desc = xmltodict.parse(nc_reply.xml)["rpc-reply"]["data"]
            acl_match = acl_desc["access-lists"]["access-list"]["access-list-entries"]["access-list-entry"]

            match_str = (
                f"For SEQ number: {acl_match['rule-name']} the number of ACE matches "
                f"is: {acl_match['access-list-entries-oper-data']['match-counter']}"
            )
            print(match_str)
            time.sleep(7)


if __name__ == '__main__':
    main()