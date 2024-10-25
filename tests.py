#!/bin/env python

from os import getenv
from pathlib import Path

from imagepig import ImagePig

IMAGEPIG_API_KEY = getenv("IMAGEPIG_API_KEY")
JANE = "https://imagepig.com/static/jane.jpeg"
MONA_LISA = "https://imagepig.com/static/mona-lisa.jpeg"


def main():
    path = Path("output")
    path.mkdir(exist_ok=True)

    imagepig = ImagePig(IMAGEPIG_API_KEY)

    imagepig.default("pig").save(path / "pig1.jpeg")
    imagepig.xl("pig").save(path / "pig2.jpeg")
    imagepig.flux("pig").save(path / "pig3.jpeg")
    imagepig.faceswap(JANE, MONA_LISA).save(path / "faceswap.jpeg")
    imagepig.upscale(JANE).save(path / "upscale.jpeg")
    imagepig.cutout(JANE).save(path / "cutout.png")
    imagepig.replace(JANE, "woman", "robot").save(path / "replace.jpeg")
    imagepig.outpaint(JANE, "dress", bottom=500).save(path / "outpaint.jpeg")


if __name__ == "__main__":
    main()
