"""
build_images.py
---------------
A tiny helper script that generates the image assets for the church website:
  - favicon.png          (browser tab icon)
  - apple-touch-icon.png (icon iPhones/iPads use when the site is saved to home screen)
  - images/next_event.png (a PLACEHOLDER sample announcement you will overwrite)

You do NOT need to run this to use the website -- the finished images are already
included in the repo. It is kept here only so you (or your student) can see exactly
how the placeholder graphics were made, and regenerate them if you ever want to.

Run it with:  python3 build_images.py
Requires the Pillow library:  pip install pillow
"""

from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Brand colors (kept identical to the values documented in the README + CSS)
# ---------------------------------------------------------------------------
OXBLOOD = (110, 20, 35)     # #6E1423  deep burgundy / liturgical red
DEEP_RED = (138, 28, 43)    # #8A1C2B  slightly brighter red
GOLD = (182, 138, 62)       # #B68A3E  antique gold
LIGHT_GOLD = (216, 190, 140)  # #D8BE8C  warm tan / light gold
CREAM = (250, 245, 234)     # #FAF5EA  ivory page background
CHARCOAL = (42, 37, 33)     # #2A2521  near-black body text


def jerusalem_cross_rects(size):
    """
    Return a list of (x0, y0, x1, y1) rectangles that, drawn together, form a
    Jerusalem Cross on a square canvas of the given `size`.

    A Jerusalem Cross = one large central "cross potent" (a cross whose four arms
    each end in a short perpendicular bar) PLUS four small plain crosses, one in
    each quadrant. It is the historic symbol used across the Anglican tradition.

    The math below is written on a 0-100 grid and then scaled to `size` so the
    same shape works at any resolution.
    """
    s = size / 100.0  # scale factor from the 0-100 grid to real pixels

    def R(x0, y0, x1, y1):
        return (x0 * s, y0 * s, x1 * s, y1 * s)

    rects = []

    # --- Central cross potent -------------------------------------------------
    rects.append(R(44, 20, 56, 80))   # vertical bar
    rects.append(R(20, 44, 80, 56))   # horizontal bar
    # the four "potent" end caps (short perpendicular bars at each arm tip)
    rects.append(R(37, 16, 63, 24))   # top cap
    rects.append(R(37, 76, 63, 84))   # bottom cap
    rects.append(R(16, 37, 24, 63))   # left cap
    rects.append(R(76, 37, 84, 63))   # right cap

    # --- Four small crosses, one per quadrant --------------------------------
    for cx, cy in [(30, 30), (70, 30), (30, 70), (70, 70)]:
        rects.append(R(cx - 3, cy - 11, cx + 3, cy + 11))  # small vertical
        rects.append(R(cx - 11, cy - 3, cx + 11, cy + 3))  # small horizontal

    return rects


def make_icon(size, path, tile=True):
    """Draw a gold Jerusalem Cross, optionally on a rounded deep-red tile."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    if tile:
        # rounded red background so the icon is visible on any browser tab color
        pad = int(size * 0.06)
        radius = int(size * 0.18)
        draw.rounded_rectangle(
            [pad, pad, size - pad, size - pad], radius=radius, fill=DEEP_RED
        )

    for r in jerusalem_cross_rects(size):
        draw.rectangle(r, fill=GOLD)

    img.save(path)
    print("wrote", path)


def load_font(size):
    """Try a few common serif fonts; fall back to PIL's default if none exist."""
    for name in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
    ]:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def centered_text(draw, cx, y, text, font, fill):
    """Draw `text` horizontally centered on x=cx at vertical position y."""
    box = draw.textbbox((0, 0), text, font=font)
    w = box[2] - box[0]
    draw.text((cx - w / 2, y), text, font=font, fill=fill)


def make_placeholder_event(path):
    """
    Build the PLACEHOLDER announcement image: a tall 5:7 portrait graphic in the
    church's red-and-gold identity. You will replace this file with your real
    event graphic (same name, images/next_event.png, same ~5:7 shape).
    """
    W, H = 1061, 1483  # exactly the 5:7 portrait ratio from the sample
    img = Image.new("RGB", (W, H), OXBLOOD)
    draw = ImageDraw.Draw(img)

    # thin gold frame just inside the edge
    m = 46
    draw.rectangle([m, m, W - m, H - m], outline=GOLD, width=6)

    # Jerusalem Cross near the top, drawn onto a small transparent layer then pasted
    cross_size = 300
    cross_layer = Image.new("RGBA", (cross_size, cross_size), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(cross_layer)
    for r in jerusalem_cross_rects(cross_size):
        cdraw.rectangle(r, fill=GOLD)
    img.paste(cross_layer, (int(W / 2 - cross_size / 2), 210), cross_layer)

    # placeholder wording (this is only a sample -- your real image replaces it)
    centered_text(draw, W / 2, 600, "SAMPLE", load_font(120), LIGHT_GOLD)
    centered_text(draw, W / 2, 740, "ANNOUNCEMENT", load_font(96), LIGHT_GOLD)

    body = load_font(52)
    centered_text(draw, W / 2, 940, "Replace this file with your", body, CREAM)
    centered_text(draw, W / 2, 1010, "own event graphic:", body, CREAM)
    centered_text(draw, W / 2, 1110, "images/next_event.png", load_font(56), GOLD)
    centered_text(draw, W / 2, 1240, "Keep it a tall 5:7 portrait shape", body, LIGHT_GOLD)

    # save compressed so the placeholder stays small and the page loads fast
    img.save(path, "PNG", optimize=True)
    print("wrote", path)


if __name__ == "__main__":
    make_icon(64, "favicon.png", tile=True)
    make_icon(180, "apple-touch-icon.png", tile=True)
    make_placeholder_event("images/next_event.png")
