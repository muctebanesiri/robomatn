import sys
import shutil
import os
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from scripts import (
    update_names,
    update_attribs,
    mkdir
)


instances = [
    {
        "attribs": {"fsSelection": 64, "macStyle": 0, "usWeightClass": 250},
        "axes": {"ital": 0.0, "wdth": 100, "wght": 100},
        "filename": "robomatn-Thin.ttf",
        "names": {
            "1,3,1,1033": "robomatn Thin",
            "16,3,1,1033": "robomatn",
            "17,3,1,1033": "Thin",
            "2,3,1,1033": "Regular",
            "3,3,1,1033": "Google:robomatn Thin:2016",
            "4,3,1,1033": "robomatn Thin",
            "6,3,1,1033": "robomatn-Thin",
        },
    },
    {
        "attribs": {"fsSelection": 513, "macStyle": 2, "usWeightClass": 250, "italicAngle": -12, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 100, "wght": 100},
        "filename": "robomatn-ThinItalic.ttf",
        "names": {
            "1,3,1,1033": "robomatn Thin",
            "16,3,1,1033": "robomatn",
            "17,3,1,1033": "Thin Italic",
            "2,3,1,1033": "Italic",
            "3,3,1,1033": "Google:robomatn Thin Italic:2016",
            "4,3,1,1033": "robomatn Thin Italic",
            "6,3,1,1033": "robomatn-ThinItalic",
        },
    },
    {
        "attribs": {"fsSelection": 64, "macStyle": 0, "usWeightClass": 300},
        "axes": {"ital": 0.0, "wdth": 100, "wght": 300},
        "filename": "robomatn-Light.ttf",
        "names": {
            "1,3,1,1033": "robomatn Light",
            "16,3,1,1033": "robomatn",
            "17,3,1,1033": "Light",
            "2,3,1,1033": "Regular",
            "3,3,1,1033": "Google:robomatn Light:2016",
            "4,3,1,1033": "robomatn Light",
            "6,3,1,1033": "robomatn-Light",
        },
    },
    {
        "attribs": {"fsSelection": 64, "macStyle": 0, "usWeightClass": 300, "usWidthClass": 3},
        "axes": {"ital": 0.0, "wdth": 75.0, "wght": 300},
        "filename": "robomatnCondensed-Light.ttf",
        "names": {
            "1,3,1,1033": "robomatn Condensed Light",
            "16,3,1,1033": "robomatn Condensed",
            "17,3,1,1033": "Light",
            "2,3,1,1033": "Regular",
            "3,3,1,1033": "Google:robomatn Condensed Light:2016",
            "4,3,1,1033": "robomatn Condensed Light",
            "6,3,1,1033": "robomatnCondensed-Light",
        },
    },
    {
        "attribs": {"fsSelection": 513, "macStyle": 2, "usWeightClass": 300, "italicAngle": -12, "usWidthClass": 3, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 75.0, "wght": 300},
        "filename": "robomatnCondensed-LightItalic.ttf",
        "names": {
            "1,3,1,1033": "robomatn Condensed Light",
            "16,3,1,1033": "robomatn Condensed",
            "17,3,1,1033": "Light Italic",
            "2,3,1,1033": "Italic",
            "3,3,1,1033": "Google:robomatn Condensed Light Italic:2016",
            "4,3,1,1033": "robomatn Condensed Light Italic",
            "6,3,1,1033": "robomatnCondensed-LightItalic",
        },
    },
    {
        "attribs": {"fsSelection": 513, "macStyle": 2, "usWeightClass": 300, "italicAngle": -12, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 100, "wght": 300},
        "filename": "robomatn-LightItalic.ttf",
        "names": {
            "1,3,1,1033": "robomatn Light",
            "16,3,1,1033": "robomatn",
            "17,3,1,1033": "Light Italic",
            "2,3,1,1033": "Italic",
            "3,3,1,1033": "Google:robomatn Light Italic:2016",
            "4,3,1,1033": "robomatn Light Italic",
            "6,3,1,1033": "robomatn-LightItalic",
        },
    },
    {
        "attribs": {"fsSelection": 64, "macStyle": 0, "usWeightClass": 400},
        "axes": {"ital": 0.0, "wdth": 100, "wght": 400},
        "filename": "robomatn-Regular.ttf",
        "names": {
            "1,3,1,1033": "robomatn",
            "2,3,1,1033": "Regular",
            "3,3,1,1033": "Google:robomatn Regular:2016",
            "4,3,1,1033": "robomatn",
            "6,3,1,1033": "robomatn-Regular",
        },
    },
    {
            "attribs": {"fsSelection": 64, "macStyle": 0, "usWeightClass": 400, "usWidthClass": 3},
        "axes": {"ital": 0.0, "wdth": 75.0, "wght": 400},
        "filename": "robomatnCondensed-Regular.ttf",
        "names": {
            "1,3,1,1033": "robomatn Condensed",
            "2,3,1,1033": "Regular",
            "3,3,1,1033": "Google:robomatn Condensed Regular:2016",
            "4,3,1,1033": "robomatn Condensed",
            "6,3,1,1033": "robomatnCondensed-Regular",
        },
    },
    {
        "attribs": {"fsSelection": 513, "macStyle": 2, "usWeightClass": 400, "italicAngle": -12, "usWidthClass": 3, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 75.0, "wght": 400},
        "filename": "robomatnCondensed-Italic.ttf",
        "names": {
            "1,3,1,1033": "robomatn Condensed",
            "2,3,1,1033": "Italic",
            "3,3,1,1033": "Google:robomatn Condensed Italic:2016",
            "4,3,1,1033": "robomatn Condensed Italic",
            "6,3,1,1033": "robomatnCondensed-Italic",
        },
    },
    {
        "attribs": {"fsSelection": 513, "macStyle": 2, "usWeightClass": 400, "italicAngle": -12, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 100, "wght": 400},
        "filename": "robomatn-Italic.ttf",
        "names": {
            "1,3,1,1033": "robomatn",
            "2,3,1,1033": "Italic",
            "3,3,1,1033": "Google:robomatn Italic:2016",
            "4,3,1,1033": "robomatn Italic",
            "6,3,1,1033": "robomatn-Italic",
        },
    },
    {
        "attribs": {"fsSelection": 64, "macStyle": 0, "usWeightClass": 500, "usWidthClass": 3},
        "axes": {"ital": 0.0, "wdth": 75.0, "wght": 500},
        "filename": "robomatnCondensed-Medium.ttf",
        "names": {
            "1,3,1,1033": "robomatn Condensed Medium",
            "2,3,1,1033": "Regular",
            "3,3,1,1033": "Google:robomatn Condensed Medium:2016",
            "4,3,1,1033": "robomatn Condensed Medium",
            "6,3,1,1033": "robomatnCondensed-Medium",
            "16,3,1,1033": "robomatn Condensed",
            "17,3,1,1033": "Medium",
        },
    },
    {
        "attribs": {"fsSelection": 64, "macStyle": 0, "usWeightClass": 500},
        "axes": {"ital": 0.0, "wdth": 100, "wght": 500},
        "filename": "robomatn-Medium.ttf",
        "names": {
            "1,3,1,1033": "robomatn Medium",
            "16,3,1,1033": "robomatn",
            "17,3,1,1033": "Medium",
            "2,3,1,1033": "Regular",
            "3,3,1,1033": "Google:robomatn Medium:2016",
            "4,3,1,1033": "robomatn Medium",
            "6,3,1,1033": "robomatn-Medium",
        },
    },
    {
        "attribs": {"fsSelection": 513, "macStyle": 2, "usWeightClass": 500, "italicAngle": -12, "usWidthClass": 3, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 75.0, "wght": 500},
        "filename": "robomatnCondensed-MediumItalic.ttf",
        "names": {
            "1,3,1,1033": "robomatn Condensed Medium",
            "2,3,1,1033": "Italic",
            "3,3,1,1033": "Google:robomatn Condensed Medium Italic:2016",
            "4,3,1,1033": "robomatn Condensed Medium Italic",
            "6,3,1,1033": "robomatnCondensed-MediumItalic",
            "16,3,1,1033": "robomatn Condensed",
            "17,3,1,1033": "Medium Italic",
        },
    },
    {
        "attribs": {"fsSelection": 513, "macStyle": 2, "usWeightClass": 500, "italicAngle": -12, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 100, "wght": 500},
        "filename": "robomatn-MediumItalic.ttf",
        "names": {
            "1,3,1,1033": "robomatn Medium",
            "16,3,1,1033": "robomatn",
            "17,3,1,1033": "Medium Italic",
            "2,3,1,1033": "Italic",
            "3,3,1,1033": "Google:robomatn Medium Italic:2016",
            "4,3,1,1033": "robomatn Medium Italic",
            "6,3,1,1033": "robomatn-MediumItalic",
        },
    },
    {
        "attribs": {"fsSelection": 32, "macStyle": 1, "usWeightClass": 700, "usWidthClass": 3},
        "axes": {"ital": 0.0, "wdth": 75.0, "wght": 700},
        "filename": "robomatnCondensed-Bold.ttf",
        "names": {
            "1,3,1,1033": "robomatn Condensed",
            "2,3,1,1033": "Bold",
            "3,3,1,1033": "Google:robomatn Condensed Bold:2016",
            "4,3,1,1033": "robomatn Condensed Bold",
            "6,3,1,1033": "robomatnCondensed-Bold",
        },
    },
    {
        "attribs": {"fsSelection": 32, "macStyle": 1, "usWeightClass": 700},
        "axes": {"ital": 0.0, "wdth": 100, "wght": 700},
        "filename": "robomatn-Bold.ttf",
        "names": {
            "1,3,1,1033": "robomatn",
            "2,3,1,1033": "Bold",
            "3,3,1,1033": "Google:robomatn Bold:2016",
            "4,3,1,1033": "robomatn Bold",
            "6,3,1,1033": "robomatn-Bold",
        },
    },
    {
        "attribs": {"fsSelection": 545, "macStyle": 3, "usWeightClass": 700, "italicAngle": -12, "usWidthClass": 3, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 75.0, "wght": 700},
        "filename": "robomatnCondensed-BoldItalic.ttf",
        "names": {
            "1,3,1,1033": "robomatn Condensed",
            "2,3,1,1033": "Bold Italic",
            "3,3,1,1033": "Google:robomatn Condensed Bold Italic:2016",
            "4,3,1,1033": "robomatn Condensed Bold Italic",
            "6,3,1,1033": "robomatnCondensed-BoldItalic",
        },
    },
    {
        "attribs": {"fsSelection": 545, "macStyle": 3, "usWeightClass": 700, "italicAngle": -12, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 100, "wght": 700},
        "filename": "robomatn-BoldItalic.ttf",
        "names": {
            "1,3,1,1033": "robomatn",
            "2,3,1,1033": "Bold Italic",
            "3,3,1,1033": "Google:robomatn Bold Italic:2016",
            "4,3,1,1033": "robomatn Bold Italic",
            "6,3,1,1033": "robomatn-BoldItalic",
        },
    },
    {
        "attribs": {"fsSelection": 64, "macStyle": 0, "usWeightClass": 900},
        "axes": {"ital": 0.0, "wdth": 100, "wght": 900},
        "filename": "robomatn-Black.ttf",
        "names": {
            "1,3,1,1033": "robomatn Black",
            "16,3,1,1033": "robomatn",
            "17,3,1,1033": "Black",
            "2,3,1,1033": "Regular",
            "3,3,1,1033": "Google:robomatn Black:2016",
            "4,3,1,1033": "robomatn Black",
            "6,3,1,1033": "robomatn-Black",
        },
    },
    {
        "attribs": {"fsSelection": 513, "macStyle": 2, "usWeightClass": 900, "italicAngle": -12, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 100, "wght": 900},
        "filename": "robomatn-BlackItalic.ttf",
        "names": {
            "1,3,1,1033": "robomatn Black",
            "16,3,1,1033": "robomatn",
            "17,3,1,1033": "Black Italic",
            "2,3,1,1033": "Italic",
            "3,3,1,1033": "Google:robomatn Black Italic:2016",
            "4,3,1,1033": "robomatn Black Italic",
            "6,3,1,1033": "robomatn-BlackItalic",
        },
    },
]


vf = TTFont(sys.argv[1])
out_dir = mkdir(sys.argv[2])

for inst in instances:
    print(f"Making {inst['filename']}")
    instance = instantiateVariableFont(vf, inst["axes"])
    update_attribs(instance, **inst["attribs"])
    update_names(instance, **inst["names"])
    del instance['STAT']
    out_path = os.path.join(sys.argv[2], inst["filename"])
    instance.save(out_path)
