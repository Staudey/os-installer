#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
#  This file is part of os-installer
#
#  Copyright 2013-2016 Ikey Doherty <ikey@solus-project.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 2 of the License, or
#  (at your option) any later version.
#

import sys
import os
from os_installer2.diskman import DiskManager, DriveProber
from os_installer2.strategy import DiskStrategyManager


def main():
    dm = DiskManager()
    dp = DriveProber(dm)

    dp.probe()

    strat = DiskStrategyManager(dp)
    for drive in dp.drives:
        ideas = strat.get_strategies(drive)
        if not ideas:
            print("Unsuitable drive: {}".format(drive.path))
            continue
        for idea in ideas:
            print("Possible strategy: {}".format(idea.get_name()))

if __name__ == "__main__":
    if os.geteuid() != 0:
        sys.stderr.write("You must be root to use OsInstaller\n")
        sys.stderr.flush()
        sys.exit(1)
    main()
