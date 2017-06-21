#!/usr/bin/env python

# http://www.apache.org/licenses/LICENSE-2.0.txt
#
# Copyright 2016 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import re

import snap_plugin.v1 as snap
from pkg_resources import get_distribution

import snap_diamond

PACKAGE_NAME = "snap-plugin-collector-diamond"


def get_plugin_version(name):
    """
    Parse plugin package version string and return major version number as integer

    :param name: The name of package
    :return: Major version number
    """
    _ver = re.search('^(\d+).*$', get_distribution(name).version)
    if _ver and len(_ver.groups()) > 0:
        return int(_ver.groups()[0])
    return 1


def run():
    snap_diamond.DiamondCollector("diamond", get_plugin_version(PACKAGE_NAME), exclusive=True,
                                  routing_strategy=snap.plugin.RoutingStrategy.sticky,
                                  concurrency_count=1).start_plugin()


if __name__ == "__main__":
    run()
