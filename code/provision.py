#! /usr/bin/env python3

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
__contributors__ = [
    "Bryan Byrne <brybyrne@cisco.com>", "Hank Preston <hapresto@cisco.com>",
]
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

from ncclient import manager, xml_
from ruamel.yaml import YAML
from lxml import etree

import constants
import utils
from utils import prettify_xml as P


def main():
    with manager.connect(
        host=constants.NC_HOST,
        port=constants.NC_PORT,
        username=constants.DEVICE_USERNAME,
        password=constants.DEVICE_PASSWORD,
        timeout=30,
        hostkey_verify=False,
    ) as nc, open("netconf_cfg/provision.yml") as f:
        yaml = YAML(typ="safe")
        data = yaml.load(f)
        xml = utils.dict_to_xml(data, root="config")
        print(f"Sending RPC:\n{P(xml)}")
        xml_str = etree.tostring(xml).decode('utf-8')
        nc_reply = nc.edit_config(xml_str, target="running")
        print(f"Received RPC reply:\n{P(nc_reply.xml)}")

        print("Saving configuration")
        nc_reply = nc.dispatch(xml_.to_ele(constants.NC_SAVE_CONFIG_RPC))
        if nc_reply.ok:
            print("Running config was saved to startup successfully")
        else:
            print("Failed to save running config to startup")


if __name__ == "__main__":
    main()
