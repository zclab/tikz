
import subprocess
from scripts.website_data import GenerateWebsiteData

src_dir = "src"
out_dir = "tikzout"
rep_url = "https://github.com/zclab/tikz/"
img_url = "https://cdn.jsdelivr.net/gh/zclab/tikz/"


webdata = GenerateWebsiteData(
    src_dir, out_dir, rep_url, img_url, branch="main")
webdata.generate_all_items_toml(output_file="website/data/items.toml")

subprocess.run("cd website && hugo --minify", shell=True)
