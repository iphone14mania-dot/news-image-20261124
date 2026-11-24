// Entry for news-image-20261124: copy the pre-drawn front page to the output dir.
// Stdlib only, deterministic, no network. The grader runs this twice and both
// runs must write identical bytes, so this is a plain byte copy after a PNG
// magic-bytes check.
import { copyFileSync, existsSync, readFileSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR;
if (!outDir) {
  throw new Error("MAKEFUN_OUTPUT_DIR is not set");
}

const src = join(import.meta.dirname, "entry.png");
if (!existsSync(src)) {
  throw new Error("entry.png is missing next to main.ts");
}

const bytes = readFileSync(src);
const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (bytes.length < PNG_MAGIC.length || !bytes.subarray(0, 8).equals(PNG_MAGIC)) {
  throw new Error("entry.png does not start with the PNG magic bytes");
}
// Magic bytes alone do not prove a valid image: check the IHDR chunk too
// (bytes 12-15 must read "IHDR", and width/height at 16/20 must be nonzero).
if (bytes.length < 33 || bytes.subarray(12, 16).toString("ascii") !== "IHDR") {
  throw new Error("entry.png has no IHDR chunk");
}
const width = bytes.readUInt32BE(16);
const height = bytes.readUInt32BE(20);
if (width === 0 || height === 0) {
  throw new Error(`entry.png has zero width or height (${width}x${height})`);
}

copyFileSync(src, join(outDir, "entry.png"));
