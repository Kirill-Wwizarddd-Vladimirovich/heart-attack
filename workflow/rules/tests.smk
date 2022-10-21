from config import raw_path, interim_path, processed_path, analysis_path, cli_path, external_path, stat_tests_path, settings


rule anomaly_df:
    input:
        raw_path/"heart.csv"
    output:
        interim_path/"features.csv",
        processed_path/"target.csv"
    params:
        cli=cli_path
    shell:
        "python {params.cli} features-target {input} {output}"


rule mutual_test:
    input:
        interim_path/"features.csv",
        external_path/"target.csv"
    output:
        stat_tests_path/"mutual_features.png",
        interim_path/"mutual_data.csv"
    params:
        cli=cli_path
    shell:
        "python {params.cli} mutual-results {input} {output}"


rule chi2_test:
    input:
        interim_path/"features.csv",
        external_path/"target.csv"
    output:
        stat_tests_path/"chi2_features.png",
        interim_path/"chi2_data.csv"
    params:
        cli=cli_path
    shell:
        "python {params.cli} chi2-results {input} {output}"


rule anova_test:
    input:
        interim_path/"features.csv",
        external_path/"target.csv"
    output:
        stat_tests_path/"anova_features.png",
        interim_path/"anova_data.csv"
    params:
        cli=cli_path
    shell:
        "python {params.cli} anova-results {input} {output}"


rule all_tests:
    input:
        rules.anomaly_df.output,
        rules.mutual_test.output,
        rules.chi2_test.output,
        rules.anova_test.output,
