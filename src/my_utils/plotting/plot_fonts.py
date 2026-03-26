from IPython.display import display, JSON
import json
import pandas as pd
import matplotlib as mpl
from matplotlib import font_manager
from pathlib import Path
from my_utils.paths import FONTS_DIR
from my_utils.printing.printing import print_configuration

FONT_NAME = "Inter_24pt-Regular.ttf"

def set_font(font_file = FONT_NAME, print_info=False):
    '''Set the font for matplotlib plots.'''
    #print("Setting font...")
    font_path = FONTS_DIR / font_file
    assert font_path.exists(), f"Font file not found: {font_path}"
    #print(f"Font path: {font_path}")
    #print("Inter" in {f.name for f in font_manager.fontManager.ttflist})
    prop = font_manager.FontProperties(fname=str(font_path))
    
    configuration = {
        "font.family": prop.get_name(),
        "font.size": 12,
        "axes.titlesize": 18,
        "axes.labelsize": 14,
        "legend.fontsize": 14,
        "xtick.labelsize": 12,
        "ytick.labelsize": 12,
        "figure.titlesize": 18
    }
    if print_info:
        print_configuration(configuration, title="Font Configuration", sort_keys=False)
    
    #print(mpl.rcParams.keys()) # Debug: print available rcParams keys

    font_manager.fontManager.addfont(font_path)
    mpl.rcParams["font.family"] = configuration["font.family"]
    mpl.rcParams["font.size"] = configuration["font.size"]
    mpl.rcParams["axes.titlesize"] = configuration["axes.titlesize"]
    mpl.rcParams["axes.labelsize"] = configuration["axes.labelsize"]
    mpl.rcParams["legend.fontsize"] = configuration["legend.fontsize"]
    mpl.rcParams["xtick.labelsize"] = configuration["xtick.labelsize"]
    mpl.rcParams["ytick.labelsize"] = configuration["ytick.labelsize"]
    mpl.rcParams["figure.titlesize"] = configuration["figure.titlesize"]

    return prop


if __name__ == "__main__":
    prop = set_font()
    print(prop.get_name())