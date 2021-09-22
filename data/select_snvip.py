#!/usr/bin/env python
# coding: utf-8

############################################################################################
# Copyright 2021 Alejandro Gomez-Garay, Bogdan Raducanu, Joaquín Salas. All Rights Reserved.
#
# License under GPLv3 (http://www.gnu.org/licenses/gpl-3.0.html)
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
############################################################################################

import os
import wget
import concurrent.futures
import argparse
import pathlib

parser = argparse.ArgumentParser(description="Select SNVIP from original SceneNet RGB-D images")
parser.add_argument(
    "--output_dir", type=str, default="", help="Output path to save images to"
)

args = parser.parse_args()
root = pathlib.Path().absolute()
assert pathlib.Path(args.output_dir).is_dir(), "not valid dir"



