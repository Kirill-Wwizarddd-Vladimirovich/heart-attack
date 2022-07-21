from pathlib import Path
categorical_feat = ['sex',  'fbs', 'exng', 'restecg',  'slp', 'cp',  'thall','caa']
numerical_feat = ['age', 'oldpeak', 'trtbps', 'thalachh', 'chol']

cli_path = Path("src/cli/cli.py")

raw_path = Path("data/raw")
interim_path = Path("data/interim")
processed_path = Path("data/processed")
#external_path = Path("data/external")
reports_path = Path("reports/figures")