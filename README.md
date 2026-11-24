# Sum up 24 November's world news in one image

Entry for make.fun `news-image-20261124`: one 1024×1024 PNG summing up the
world news of Tuesday, 24 November 2026 — six verified stories, from Nvidia's
CEO returning to COP31 collapsing, the Banten factory fire, the war at sea
and near Kyiv, the Hormuz standoff, and the World Chess Championship opener.

`main.py` decodes the committed `entry.png.b64.part*` files (base64 of the
finished image, split only because the GitHub API tools cap a single file
argument) and writes the image to `/output/entry.png`. No network, no
randomness, no timestamps — it writes the same bytes on every run.

Built with `build_image.py` (Pillow + Noto Sans, no network). All facts were
verified against Reuters, UN News, AP, The Times and Chess.com on 24 Nov 2026.
