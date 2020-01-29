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

from netmiko import ConnectHandler

import constants


def main():
    with ConnectHandler(**constants.NETMIKO_CONN_PARAMS) as ch:
        ping_gdns = ch.send_command("ping 8.8.8.8 repeat 10")
        ping_odns = ch.send_command("ping 208.67.222.222 repeat 200")
        print(ping_gdns)
        print(ping_odns)


if __name__ == "__main__":
    main()
