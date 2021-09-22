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
#import wget
import concurrent.futures
import argparse
import pathlib
import tarfile

parser = argparse.ArgumentParser(description="Download SceneNet data: images, ")
parser.add_argument(
    "--output_dir", type=str, default="", help="Output file to save images to"
)

args = parser.parse_args()
root = pathlib.Path().absolute()
assert pathlib.Path(args.output_dir).is_dir(), "not valid dir"

fls_ids = [
"train_split/train_0",
"train_split/train_1",
"train_split/train_2",
"train_split/train_3",
"train_split/train_4",
"train_split/train_5",
"train_split/train_6",
"train_split/train_7",
"train_split/train_8",
"train_split/train_9",
"train_split/train_10",
"train_split/train_11",
"train_split/train_12",
"train_split/train_13",
"train_split/train_14",
"train_split/train_15",
"train_split/train_16",
"SceneNetRGBD-val"]


def download_files(id):
    start_url = "https://www.doc.ic.ac.uk/~bjm113/scenenet_data/"
    filename = "{}".format(id)
    filename = filename + ".tar.gz"
    full_url = os.path.join(start_url, filename)
    wget.download(full_url, out=args.output_dir)
    #print(full_url)

def extract_files(id):
    filename = "{}".format(id)
    filename = output_dir + filename + ".tar.gz"
    atar = tarfile.open(filename)
    atar.extractall(output_dir) # specify which folder to extract to
    atar.close()
    #print(filename)

#download_files(fls_ids[0])
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_files, fls_ids)
    
# Extract data to output_dir
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extract_files, fls_ids)
    


