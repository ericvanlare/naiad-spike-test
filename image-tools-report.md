# Image Processing Tools Availability Report

**Environment:** Linux (Ubuntu 24.04, x86_64, Azure-hosted runner)  
**Date:** 2026-03-05

---

## Summary

| Tool | Available? | Notes |
|------|-----------|-------|
| `sips` | ❌ **No** | macOS-only tool; not available on Linux |
| `magick` (ImageMagick 7) | ❌ **No** | Not packaged for Ubuntu 24.04 |
| `convert` (ImageMagick 6) | ✅ **Yes** | Works after installing `imagemagick` package |

---

## `sips` — Scriptable Image Processing System

**Status: Not available**

`sips` is an Apple/macOS-exclusive command-line tool bundled with macOS. It is not available on Linux and there is no port or equivalent package. Since this environment runs Linux (Ubuntu 24.04 on Azure), `sips` cannot be used here under any circumstances.

---

## `magick` — ImageMagick 7 CLI

**Status: Not available**

The `magick` command is the unified CLI for **ImageMagick 7**. Ubuntu 24.04's repositories only ship **ImageMagick 6** (version `6.9.12-98 Q16`). There is no `magick` binary available via `apt`.

To get ImageMagick 7 in this environment, you would need to either:
- Compile from source ([imagemagick.org](https://imagemagick.org))
- Use a third-party PPA or AppImage
- Run it via a container

None of these are pre-installed.

---

## `convert` (and friends) — ImageMagick 6 CLI

**Status: ✅ Fully functional**

ImageMagick 6 libraries (`libmagickcore`, `libmagickwand`) were already pre-installed in the environment. After installing the `imagemagick` package (`apt-get install imagemagick`), the full suite of IM6 CLI tools became available:

| Command | Path |
|---------|------|
| `convert` | `/usr/bin/convert-im6.q16` |
| `identify` | `/usr/bin/identify-im6.q16` |
| `mogrify` | `/usr/bin/mogrify-im6.q16` |
| `composite` | `/usr/bin/composite-im6.q16` |
| `compare` | `/usr/bin/compare-im6.q16` |
| `montage` | `/usr/bin/montage-im6.q16` |
| `animate` | `/usr/bin/animate-im6.q16` |
| `conjure` | `/usr/bin/conjure-im6.q16` |
| `display` | `/usr/bin/display-im6.q16` |
| `import` | `/usr/bin/import-im6.q16` |
| `stream` | `/usr/bin/stream-im6.q16` |

**Version:** `ImageMagick 6.9.12-98 Q16 x86_64`

### Functional Tests Performed (all passed ✅)

| Test | Command | Result |
|------|---------|--------|
| Create solid color image | `convert -size 100x100 xc:red out.png` | `PNG 100x100, 171B` |
| Resize | `convert -size 200x200 xc:blue -resize 50x50 out.png` | `PNG 50x50, 165B` |
| Format conversion (PNG→JPEG) | `convert in.png out.jpg` | `JPEG 100x100, 415B` |
| Drawing primitives | `convert -size 100x100 xc:green -fill yellow -draw "circle 50,50 50,10" out.png` | `PNG 100x100, 2623B` |
| Text annotation | `convert -size 200x50 xc:white -pointsize 20 -annotate +10+30 "Hello World" out.png` | `PNG 200x50, 888B` |

### Supported Delegates (built-in)

`bzlib djvu fftw fontconfig freetype heic jbig jng jp2 jpeg lcms lqr ltdl lzma openexr pangocairo png raw tiff webp wmf x xml zlib`

This means the installed ImageMagick can read/write most common formats including PNG, JPEG, WebP, TIFF, HEIC, JP2, and more.

---

## Recommendations

- **If you need `sips` functionality:** Use `convert`/`mogrify` from ImageMagick 6 as a drop-in replacement for most operations (resize, rotate, format conversion, metadata queries via `identify`).
- **If you specifically need the `magick` command:** Create an alias (`alias magick=convert`) for basic compatibility, or build ImageMagick 7 from source.
- **For this environment**, ImageMagick 6 via `convert` is the practical choice and is fully operational.
