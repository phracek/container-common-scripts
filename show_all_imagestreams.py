#!/bin/env python3

# MIT License
#
# Copyright (c) 2018-2019 Red Hat, Inc.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
import os

from pathlib import Path
from typing import Dict, Any

IMAGESTREAMS_DIR: str = "imagestreams"


class ShowAllImageStreams(object):
    version: str = ""

    def __init__(self):
        pass

    def load_json_file(self, filename: Path) -> Any:
        with open(str(filename)) as f:
            data = json.load(f)
            isinstance(data, Dict)
            return data

    def show_all_imagestreams(self):
        p = Path(".")
        json_files = p.glob(f"{IMAGESTREAMS_DIR}/*.json")
        if not json_files:
            print(f"No json files present in {IMAGESTREAMS_DIR}.")
            return 0
        for f in json_files:
            if os.environ.get("TARGET") in ("rhel7", "centos7") and "aarch64" in str(f):
                print("Imagestream aarch64 is not supported on rhel7")
                continue
            json_dict = self.load_json_file(f)
            print(f"Tags in the image stream {f}:")
            for tag in json_dict["spec"]["tags"]:
                print(f"- {tag['name']} -> {tag['from']['name']}")


if __name__ == "__main__":
    isc = ShowAllImageStreams()
    isc.show_all_imagestreams()
