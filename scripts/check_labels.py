import os
import pandas as pd

for lang in ["tamil", "malayalam"]:
    print("\nChecking:", lang)
    df = pd.read_csv(f"data/{lang}/labels.csv")
    audio_dir = f"data/{lang}/audio"

    print("Class distribution:")
    print(df.label.value_counts())

    missing = [f for f in df.filename if not os.path.exists(os.path.join(audio_dir, f))]
    print("Missing files:", len(missing))
