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

---
---

# Image Compression Capabilities Report

**Environment:** Linux (Ubuntu 24.04, x86_64, Azure-hosted runner)  
**Date:** 2026-03-05

## TL;DR — What Can I Do With Your Image?

If you hand me an image in this repo, I can compress it using **8 different tools** across **6 distinct strategies**. Depending on your tolerance for quality loss and format changes, I can reduce file sizes anywhere from a **modest 1%** to an **aggressive 99%**.

---

## Available Compression Tools

All tools below were installed and verified functional in this environment.

| Tool | Version | Type | Formats | Install |
|------|---------|------|---------|---------|
| **optipng** | 0.7.8 | Lossless PNG optimizer | PNG | `apt` |
| **pngquant** | 2.18.0 | Lossy PNG quantizer | PNG | `apt` |
| **jpegoptim** | 1.4.7 | JPEG optimizer | JPEG | `apt` |
| **gifsicle** | 1.94 | GIF optimizer | GIF | `apt` |
| **cwebp** | 1.3.2 | WebP encoder | PNG/JPEG/TIFF → WebP | `apt` |
| **convert** (ImageMagick 6) | 6.9.12-98 | Swiss-army knife | Everything | `apt` |
| **Pillow** (Python) | 12.1.1 | Programmatic image library | Everything | `pip` |

---

## Compression Strategies

### 1. 🟢 Lossless Optimization (same format, zero quality loss)

**What it does:** Re-encodes the file with better compression algorithms and strips unnecessary metadata. Pixel-perfect identical output.

| Tool | Best for | Command |
|------|----------|---------|
| `optipng -o7` | PNG | `optipng -o7 image.png` |
| `jpegoptim --strip-all` | JPEG | `jpegoptim --strip-all image.jpg` |
| `gifsicle -O3` | GIF | `gifsicle -O3 image.gif -o output.gif` |
| `convert -strip` | Any | `convert image.png -strip output.png` |

**Typical savings:** 1–15% (modest but risk-free)

### 2. 🟡 Lossy Quality Reduction (same format, tunable quality loss)

**What it does:** Re-encodes at a lower quality setting. Visually imperceptible at high quality values (80–90), noticeable at lower values.

| Tool | Best for | Command |
|------|----------|---------|
| `pngquant` | PNG (reduces to 256-color palette) | `pngquant --quality=65-80 --force image.png` |
| `jpegoptim --max=N` | JPEG | `jpegoptim --max=80 --strip-all image.jpg` |
| `convert -quality N` | JPEG/WebP | `convert image.jpg -quality 80 output.jpg` |
| Pillow `quality=N` | JPEG | `img.save('out.jpg', quality=80, optimize=True)` |

**Typical savings:** 40–90%

### 3. 🟠 Format Conversion (change format for better compression)

**What it does:** Converts to a more efficient format. WebP is the biggest win — it typically beats both PNG and JPEG.

| Conversion | Tool | Command |
|------------|------|---------|
| PNG → WebP | `cwebp` | `cwebp -q 80 image.png -o image.webp` |
| PNG → JPEG | `convert` | `convert image.png -quality 85 image.jpg` |
| JPEG → WebP | `cwebp` | `cwebp -q 80 image.jpg -o image.webp` |
| Any → WebP | `convert` | `convert image.png -quality 80 image.webp` |

**Typical savings:** 60–98% (PNG→WebP), 30–50% (JPEG→WebP)

> ⚠️ **Caveat:** PNG→JPEG loses transparency. WebP support is near-universal in modern browsers but not in all legacy contexts.

### 4. 🔴 Resizing / Downscaling (reduce pixel dimensions)

**What it does:** Reduces the image dimensions. A 4000×3000 photo displayed at 800×600 is wasting ~95% of its pixels.

| Tool | Command |
|------|---------|
| `convert -resize` | `convert image.png -resize 50% output.png` |
| `convert -resize WxH` | `convert image.png -resize 800x600 output.png` |
| Pillow | `img.thumbnail((800, 600)); img.save(...)` |

**Typical savings:** 50–90% (proportional to area reduction)

### 5. 🟣 Color Depth Reduction (reduce color palette)

**What it does:** Reduces the number of distinct colors. Effective for graphics/icons, less so for photographs.

| Tool | Command |
|------|---------|
| `convert -colors N` | `convert image.png -colors 256 output.png` |
| `pngquant N` | `pngquant 128 image.png` |

**Typical savings:** 50–75%

### 6. 🔵 Combined / Multi-Pass (stack techniques for maximum compression)

**What it does:** Chains multiple strategies. This is where the biggest wins happen.

Example pipeline:
```bash
# Resize + format convert + quality reduction + strip metadata
convert original.png -resize 800x600 -quality 80 -strip output.jpg

# PNG: quantize then optimize
pngquant 256 --force --output temp.png original.png && optipng -o7 temp.png

# Maximum WebP compression
cwebp -q 75 -m 6 -resize 800 600 original.png -o output.webp
```

**Typical savings:** 95–99%

---

## Benchmark Results

Tested on a generated 800×600 PNG plasma fractal image (2,554,463 bytes):

| Method | Output File | Size | % of Original | Reduction |
|--------|-------------|------|---------------|-----------|
| **Original** | `test_original.png` | **2,554,463 B** | 100% | — |
| optipng -o7 (lossless) | `.png` | 2,544,219 B | 99.6% | 0.4% |
| Metadata strip | `.png` | 2,554,401 B | ~100% | ~0% |
| Pillow optimize (lossless) | `.png` | 838,138 B | 32.8% | 67% |
| Color reduction (256) | `.png` | 708,672 B | 27.7% | 72% |
| Resize 50% | `.png` | 627,281 B | 24.6% | 75% |
| pngquant (lossy, 128 colors) | `.png` | 218,523 B | 8.6% | 91% |
| JPEG q85 | `.jpg` | 80,164 B | 3.1% | 97% |
| Progressive JPEG q85 | `.jpg` | 77,623 B | 3.0% | 97% |
| jpegoptim q80 + strip | `.jpg` | 73,622 B | 2.9% | 97% |
| Pillow JPEG q80 | `.jpg` | 65,371 B | 2.6% | 97% |
| **WebP q80** | `.webp` | **47,604 B** | **1.9%** | **98%** |
| **Resize 50% + JPEG q80** | `.jpg` | **17,267 B** | **0.7%** | **99.3%** |

---

## What I'd Do With Your Image (Decision Tree)

```
Is the image in this repo?
├── YES
│   ├── What format is it?
│   │   ├── PNG
│   │   │   ├── Is transparency needed?
│   │   │   │   ├── YES → pngquant + optipng (keep PNG, ~90% smaller)
│   │   │   │   └── NO  → convert to WebP or JPEG (~97-98% smaller)
│   │   │   └── Is it a photo or graphic/icon?
│   │   │       ├── Photo → JPEG or WebP conversion is best
│   │   │       └── Graphic → pngquant color reduction is best
│   │   ├── JPEG
│   │   │   ├── jpegoptim --strip-all (lossless, quick win)
│   │   │   ├── jpegoptim --max=80 (lossy, bigger win)
│   │   │   └── cwebp → WebP (if format change OK, ~30-50% more savings)
│   │   ├── GIF
│   │   │   ├── gifsicle -O3 (lossless)
│   │   │   └── Convert to WebP if not animated
│   │   ├── WebP → Already efficient; can try lower -q value
│   │   └── BMP/TIFF → Convert to literally anything else
│   └── Is it oversized for its use case?
│       ├── YES → Resize first, then compress
│       └── NO  → Compress at current dimensions
└── NO → Give me the image and I'll figure it out!
```

---

## Limitations & Caveats

| Limitation | Details |
|------------|---------|
| **No AVIF support** | `cavif`/`avifenc` not available. AVIF would beat WebP by another ~20-30% but requires manual compilation. |
| **No MozJPEG** | `cjpeg` from MozJPEG not installed. It produces ~10% smaller JPEGs than libjpeg. Available via manual build. |
| **No GPU acceleration** | All compression is CPU-only. Fine for individual images, slow for batch processing of thousands. |
| **pngquant quality ranges can fail** | On images with very high color complexity, pngquant may refuse to compress if it can't meet the quality floor. Omit `--quality` or use a fixed color count instead. |
| **ImageMagick 6 policy limits** | Default policy is "open" (no restrictions), but some environments restrict pixel counts, file sizes, or codecs. |
| **WebP max dimensions** | WebP has a hard limit of 16383×16383 pixels. |
| **I can view images** | The `read` tool supports JPG, PNG, GIF, and WebP, so I can actually look at your image and make an informed recommendation about quality tradeoffs. |

---

## Quick-Reference Commands

```bash
# === LOSSLESS (safe, no quality loss) ===
optipng -o7 image.png                              # Optimize PNG
jpegoptim --strip-all image.jpg                     # Strip JPEG metadata
gifsicle -O3 -o output.gif input.gif                # Optimize GIF

# === LOSSY (tunable quality) ===
pngquant --quality=65-80 --force image.png          # Lossy PNG
jpegoptim --max=80 --strip-all image.jpg            # Reduce JPEG quality
convert image.png -quality 80 output.jpg            # PNG→JPEG

# === FORMAT CONVERSION ===
cwebp -q 80 image.png -o image.webp                # → WebP (best ratio)
convert image.png image.jpg                         # → JPEG

# === RESIZE ===
convert image.png -resize 800x600 output.png       # Fit within 800x600
convert image.png -resize 50% output.png            # Half dimensions

# === MAXIMUM COMPRESSION ===
convert input.png -resize 800x600 -strip -quality 75 output.webp
cwebp -q 75 -m 6 -resize 800 600 input.png -o output.webp
```
