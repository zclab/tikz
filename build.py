
import argparse
from scripts.website_data import GenerateWebsiteData

src_dir = "src"
out_dir = "out"
rep_url = "https://github.com/zclab/tikz/"
img_url = "https://cdn.jsdelivr.net/gh/zclab/tikz/out/"


gwd = GenerateWebsiteData(src_dir, out_dir, rep_url, img_url)
gwd.get_all_items()
