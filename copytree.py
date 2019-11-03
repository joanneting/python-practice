import argparse
import shutil
parser = argparse.ArgumentParser(description='copy file')
parser.add_argument('fromHere',help='copy from here')
parser.add_argument('toHere',help='copy to here')

args = parser.parse_args()
fromHere = args.fromHere
toHere = args.toHere
# 若該目錄已有相同資料夾，無法使用copytree
shutil.copytree(fromHere,toHere)