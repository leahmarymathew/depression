import os
import pandas as pd
import shutil


def copy_and_label(src_dir, out_dir, label):
    # Copy wav files from src_dir into out_dir/audio and collect filenames/labels.
    rows = []
    for fname in os.listdir(src_dir):
        if fname.endswith(".wav"):
            shutil.copy(os.path.join(src_dir, fname), os.path.join(out_dir, "audio", fname))
            rows.append([fname, label])
    return rows


def prepare(language, depressed_subdir, non_depressed_subdir):
    base = os.path.join("raw_downloads", language, language)
    out_dir = os.path.join("data", language)
    os.makedirs(os.path.join(out_dir, "audio"), exist_ok=True)

    depressed_path = os.path.join(base, depressed_subdir, "Train_set")
    non_depressed_path = os.path.join(base, non_depressed_subdir, "Train_set")

    if not os.path.isdir(depressed_path):
        raise FileNotFoundError(f"Missing depressed path: {depressed_path}")
    if not os.path.isdir(non_depressed_path):
        raise FileNotFoundError(f"Missing non-depressed path: {non_depressed_path}")

    rows = []
    rows += copy_and_label(depressed_path, out_dir, 1)
    rows += copy_and_label(non_depressed_path, out_dir, 0)

    df = pd.DataFrame(rows, columns=["filename", "label"])
    df.to_csv(os.path.join(out_dir, "labels.csv"), index=False)
    print(language, "files:", len(df))


prepare("Tamil", "Depressed", "Non-depressed")
prepare("Malayalam", "Depressed", "Non_depressed")
