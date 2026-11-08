# NOTE: Lesson 9 (optional). Jawad skipped this lesson. Claude added this file
#       at Jawad's request, copied from the course: 02-vector-search/embed/download.py
"""Lesson 9: download an ONNX embedding model (run once).

Simple version: instead of the big PyTorch "machine", we download a small,
ready-made copy of the same model (model.onnx) plus its word-splitter
(tokenizer.json) from HuggingFace, into the models/ folder.

Run from this folder:  uv run python download.py
"""
import os
import shutil
import logging
from pathlib import Path
from huggingface_hub import hf_hub_download, list_repo_files

os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)

ONNX_CANDIDATES = [
    "onnx/model.onnx",
    "onnx/encoder_model.onnx",
    "model.onnx",
]

def download(repo, dest="models"):
    dest = Path(dest) / repo
    dest.mkdir(parents=True, exist_ok=True)

    files = list_repo_files(repo_id=repo)
    onnx_file = next((c for c in ONNX_CANDIDATES if c in files), None)
    if not onnx_file:
        raise FileNotFoundError(f"No ONNX model found in {repo}")

    for remote, local in [
        ("tokenizer.json", "tokenizer.json"),
        (onnx_file, "model.onnx"),
    ]:
        src = hf_hub_download(repo_id=repo, filename=remote)
        dst = dest / local
        if not dst.exists():
            shutil.copy2(src, dst)
            print(f"  saved {dst}")
        else:
            print(f"  exists {dst}")

    onnx_ext = onnx_file + "_data"
    if onnx_ext in files:
        src = hf_hub_download(repo_id=repo, filename=onnx_ext)
        dst = dest / "model.onnx_data"
        if not dst.exists():
            shutil.copy2(src, dst)
            print(f"  saved {dst}")
        else:
            print(f"  exists {dst}")

if __name__ == "__main__":
    download("Xenova/all-MiniLM-L6-v2")
