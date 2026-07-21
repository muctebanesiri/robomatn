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
        "filename": "roboto-Thin.ttf",
        "names": {
            "1,3,1,1033": "roboto Thin",
            "16,3,1,1033": "roboto",
            "17,3,1,1033": "Thin",
            "2,3,1,1033": "Regular",
            "3,3,1,1033": "Google:roboto Thin:2016",
            "4,3,1,1033": "roboto Thin",
            "6,3,1,1033": "roboto-Thin",
        },
    },
    {
        "attribs": {"fsSelection": 513, "macStyle": 2, "usWeightClass": 250, "italicAngle": -12, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 100, "wght": 100},
        "filename": "roboto-ThinItalic.ttf",
        "names": {
            "1,3,1,1033": "roboto Thin",
            "16,3,1,1033": "roboto",
            "17,3,1,1033": "Thin Italic",
            "2,3,1,1033": "Italic",
            "3,3,1,1033": "Google:roboto Thin Italic:2016",
            "4,3,1,1033": "roboto Thin Italic",
            "6,3,1,1033": "roboto-ThinItalic",
        },
    },
    {
        "attribs": {"fsSelection": 64, "macStyle": 0, "usWeightClass": 300},
        "axes": {"ital": 0.0, "wdth": 100, "wght": 300},
        "filename": "roboto-Light.ttf",
        "names": {
            "1,3,1,1033": "roboto Light",
            "16,3,1,1033": "roboto",
            "17,3,1,1033": "Light",
            "2,3,1,1033": "Regular",
            "3,3,1,1033": "Google:roboto Light:2016",
            "4,3,1,1033": "roboto Light",
            "6,3,1,1033": "roboto-Light",
        },
    },
    {
        "attribs": {"fsSelection": 64, "macStyle": 0, "usWeightClass": 300, "usWidthClass": 3},
        "axes": {"ital": 0.0, "wdth": 75.0, "wght": 300},
        "filename": "robotoCondensed-Light.ttf",
        "names": {
            "1,3,1,1033": "roboto Condensed Light",
            "16,3,1,1033": "roboto Condensed",
            "17,3,1,1033": "Light",
            "2,3,1,1033": "Regular",
            "3,3,1,1033": "Google:roboto Condensed Light:2016",
            "4,3,1,1033": "roboto Condensed Light",
            "6,3,1,1033": "robotoCondensed-Light",
        },
    },
    {
        "attribs": {"fsSelection": 513, "macStyle": 2, "usWeightClass": 300, "italicAngle": -12, "usWidthClass": 3, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 75.0, "wght": 300},
        "filename": "robotoCondensed-LightItalic.ttf",
        "names": {
            "1,3,1,1033": "roboto Condensed Light",
            "16,3,1,1033": "roboto Condensed",
            "17,3,1,1033": "Light Italic",
            "2,3,1,1033": "Italic",
            "3,3,1,1033": "Google:roboto Condensed Light Italic:2016",
            "4,3,1,1033": "roboto Condensed Light Italic",
            "6,3,1,1033": "robotoCondensed-LightItalic",
        },
    },
    {
        "attribs": {"fsSelection": 513, "macStyle": 2, "usWeightClass": 300, "italicAngle": -12, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 100, "wght": 300},
        "filename": "roboto-LightItalic.ttf",
        "names": {
            "1,3,1,1033": "roboto Light",
            "16,3,1,1033": "roboto",
            "17,3,1,1033": "Light Italic",
            "2,3,1,1033": "Italic",
            "3,3,1,1033": "Google:roboto Light Italic:2016",
            "4,3,1,1033": "roboto Light Italic",
            "6,3,1,1033": "roboto-LightItalic",
        },
    },
    {
        "attribs": {"fsSelection": 64, "macStyle": 0, "usWeightClass": 400},
        "axes": {"ital": 0.0, "wdth": 100, "wght": 400},
        "filename": "roboto-Regular.ttf",
        "names": {
            "1,3,1,1033": "roboto",
            "2,3,1,1033": "Regular",
            "3,3,1,1033": "Google:roboto Regular:2016",
            "4,3,1,1033": "roboto",
            "6,3,1,1033": "roboto-Regular",
        },
    },
    {
            "attribs": {"fsSelection": 64, "macStyle": 0, "usWeightClass": 400, "usWidthClass": 3},
        "axes": {"ital": 0.0, "wdth": 75.0, "wght": 400},
        "filename": "robotoCondensed-Regular.ttf",
        "names": {
            "1,3,1,1033": "roboto Condensed",
            "2,3,1,1033": "Regular",
            "3,3,1,1033": "Google:roboto Condensed Regular:2016",
            "4,3,1,1033": "roboto Condensed",
            "6,3,1,1033": "robotoCondensed-Regular",
        },
    },
    {
        "attribs": {"fsSelection": 513, "macStyle": 2, "usWeightClass": 400, "italicAngle": -12, "usWidthClass": 3, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 75.0, "wght": 400},
        "filename": "robotoCondensed-Italic.ttf",
        "names": {
            "1,3,1,1033": "roboto Condensed",
            "2,3,1,1033": "Italic",
            "3,3,1,1033": "Google:roboto Condensed Italic:2016",
            "4,3,1,1033": "roboto Condensed Italic",
            "6,3,1,1033": "robotoCondensed-Italic",
        },
    },
    {
        "attribs": {"fsSelection": 513, "macStyle": 2, "usWeightClass": 400, "italicAngle": -12, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 100, "wght": 400},
        "filename": "roboto-Italic.ttf",
        "names": {
            "1,3,1,1033": "roboto",
            "2,3,1,1033": "Italic",
            "3,3,1,1033": "Google:roboto Italic:2016",
            "4,3,1,1033": "roboto Italic",
            "6,3,1,1033": "roboto-Italic",
        },
    },
    {
        "attribs": {"fsSelection": 64, "macStyle": 0, "usWeightClass": 500, "usWidthClass": 3},
        "axes": {"ital": 0.0, "wdth": 75.0, "wght": 500},
        "filename": "robotoCondensed-Medium.ttf",
        "names": {
            "1,3,1,1033": "roboto Condensed Medium",
            "2,3,1,1033": "Regular",
            "3,3,1,1033": "Google:roboto Condensed Medium:2016",
            "4,3,1,1033": "roboto Condensed Medium",
            "6,3,1,1033": "robotoCondensed-Medium",
            "16,3,1,1033": "roboto Condensed",
            "17,3,1,1033": "Medium",
        },
    },
    {
        "attribs": {"fsSelection": 64, "macStyle": 0, "usWeightClass": 500},
        "axes": {"ital": 0.0, "wdth": 100, "wght": 500},
        "filename": "roboto-Medium.ttf",
        "names": {
            "1,3,1,1033": "roboto Medium",
            "16,3,1,1033": "roboto",
            "17,3,1,1033": "Medium",
            "2,3,1,1033": "Regular",
            "3,3,1,1033": "Google:roboto Medium:2016",
            "4,3,1,1033": "roboto Medium",
            "6,3,1,1033": "roboto-Medium",
        },
    },
    {
        "attribs": {"fsSelection": 513, "macStyle": 2, "usWeightClass": 500, "italicAngle": -12, "usWidthClass": 3, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 75.0, "wght": 500},
        "filename": "robotoCondensed-MediumItalic.ttf",
        "names": {
            "1,3,1,1033": "roboto Condensed Medium",
            "2,3,1,1033": "Italic",
            "3,3,1,1033": "Google:roboto Condensed Medium Italic:2016",
            "4,3,1,1033": "roboto Condensed Medium Italic",
            "6,3,1,1033": "robotoCondensed-MediumItalic",
            "16,3,1,1033": "roboto Condensed",
            "17,3,1,1033": "Medium Italic",
        },
    },
    {
        "attribs": {"fsSelection": 513, "macStyle": 2, "usWeightClass": 500, "italicAngle": -12, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 100, "wght": 500},
        "filename": "roboto-MediumItalic.ttf",
        "names": {
            "1,3,1,1033": "roboto Medium",
            "16,3,1,1033": "roboto",
            "17,3,1,1033": "Medium Italic",
            "2,3,1,1033": "Italic",
            "3,3,1,1033": "Google:roboto Medium Italic:2016",
            "4,3,1,1033": "roboto Medium Italic",
            "6,3,1,1033": "roboto-MediumItalic",
        },
    },
    {
        "attribs": {"fsSelection": 32, "macStyle": 1, "usWeightClass": 700, "usWidthClass": 3},
        "axes": {"ital": 0.0, "wdth": 75.0, "wght": 700},
        "filename": "robotoCondensed-Bold.ttf",
        "names": {
            "1,3,1,1033": "roboto Condensed",
            "2,3,1,1033": "Bold",
            "3,3,1,1033": "Google:roboto Condensed Bold:2016",
            "4,3,1,1033": "roboto Condensed Bold",
            "6,3,1,1033": "robotoCondensed-Bold",
        },
    },
    {
        "attribs": {"fsSelection": 32, "macStyle": 1, "usWeightClass": 700},
        "axes": {"ital": 0.0, "wdth": 100, "wght": 700},
        "filename": "roboto-Bold.ttf",
        "names": {
            "1,3,1,1033": "roboto",
            "2,3,1,1033": "Bold",
            "3,3,1,1033": "Google:roboto Bold:2016",
            "4,3,1,1033": "roboto Bold",
            "6,3,1,1033": "roboto-Bold",
        },
    },
    {
        "attribs": {"fsSelection": 545, "macStyle": 3, "usWeightClass": 700, "italicAngle": -12, "usWidthClass": 3, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 75.0, "wght": 700},
        "filename": "robotoCondensed-BoldItalic.ttf",
        "names": {
            "1,3,1,1033": "roboto Condensed",
            "2,3,1,1033": "Bold Italic",
            "3,3,1,1033": "Google:roboto Condensed Bold Italic:2016",
            "4,3,1,1033": "roboto Condensed Bold Italic",
            "6,3,1,1033": "robotoCondensed-BoldItalic",
        },
    },
    {
        "attribs": {"fsSelection": 545, "macStyle": 3, "usWeightClass": 700, "italicAngle": -12, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 100, "wght": 700},
        "filename": "roboto-BoldItalic.ttf",
        "names": {
            "1,3,1,1033": "roboto",
            "2,3,1,1033": "Bold Italic",
            "3,3,1,1033": "Google:roboto Bold Italic:2016",
            "4,3,1,1033": "roboto Bold Italic",
            "6,3,1,1033": "roboto-BoldItalic",
        },
    },
    {
        "attribs": {"fsSelection": 64, "macStyle": 0, "usWeightClass": 900},
        "axes": {"ital": 0.0, "wdth": 100, "wght": 900},
        "filename": "roboto-Black.ttf",
        "names": {
            "1,3,1,1033": "roboto Black",
            "16,3,1,1033": "roboto",
            "17,3,1,1033": "Black",
            "2,3,1,1033": "Regular",
            "3,3,1,1033": "Google:roboto Black:2016",
            "4,3,1,1033": "roboto Black",
            "6,3,1,1033": "roboto-Black",
        },
    },
    {
        "attribs": {"fsSelection": 513, "macStyle": 2, "usWeightClass": 900, "italicAngle": -12, "caretSlopeRise": 2048, "caretSlopeRun": 435},
        "axes": {"ital": 1.0, "wdth": 100, "wght": 900},
        "filename": "roboto-BlackItalic.ttf",
        "names": {
            "1,3,1,1033": "roboto Black",
            "16,3,1,1033": "roboto",
            "17,3,1,1033": "Black Italic",
            "2,3,1,1033": "Italic",
            "3,3,1,1033": "Google:roboto Black Italic:2016",
            "4,3,1,1033": "roboto Black Italic",
            "6,3,1,1033": "roboto-BlackItalic",
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
