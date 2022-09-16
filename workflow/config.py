from pathlib import Path

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["workflow/settings.toml"],
    environments=True,
)

cli_path = Path("src/cli")

raw_path = Path("data/raw")
interim_path = Path("data/interim")
processed_path = Path("data/processed")
external_path = Path("data/external")
analysis_path = Path("reports/figures/data_analysis")
stat_tests_path = Path("reports/figures")
