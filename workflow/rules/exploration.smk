from config import raw_path, interim_path, processed_path, analysis_path, cli_path, external_path, settings


rule info_extracting:
    input:
        raw_path/"heart.csv"
    output:
        analysis_path/"info.csv",
        analysis_path/"head.csv",
        analysis_path/"describe.csv"
    params:
        cli=cli_path
    shell:
        "python {params.cli} total-info {input} {output}"


rule hist_creating:
    input:
        raw_path/"heart.csv"
    output:
        analysis_path/"{numerical_feature}_histplot.png"
    params:
        cli=cli_path
    shell:
        "python {params.cli} h-plots {input} {output} {wildcards.numerical_feature}"

rule box_creating:
    input:
        raw_path/"heart.csv"
    output:
        analysis_path/"{numerical_feature}_boxplot.png"
    params:
        cli=cli_path
    shell:
        "python {params.cli} b-plots {input} {output} {wildcards.numerical_feature}"

rule count_creating:
    input:
        raw_path/"heart.csv"
    output:
        analysis_path/"{categorical_feature}_countplot.png"
    params:
        cli=cli_path
    shell:
        "python {params.cli} c-plots {input} {output} {wildcards.categorical_feature}"

rule heatmap_creating:
    input:
        raw_path/"heart.csv"
    output:
        analysis_path/"heatmap.png"
    params:
        cli=cli_path
    shell:
        "python {params.cli} heat-plots {input} {output}"

rule pairplot_creating:
    input:
        raw_path/"heart.csv"
    output:
        analysis_path/"pairplots.png"
    params:
        cli=cli_path
    shell:
        "python {params.cli} pair-plots {input} {output}"

rule anomaly_df:
    input:
        raw_path/"heart.csv"
    output:
        interim_path/"features.csv",
        external_path/"target.csv"
    params:
        cli=cli_path
    shell:
        "python {params.cli} features-target {input} {output}"

rule all_exploration:
    input:
        rules.info_extracting.output,
        expand(rules.hist_creating.output, numerical_feature = settings.numerical_feat),
        expand(rules.box_creating.output, numerical_feature = settings.numerical_feat),
        expand(rules.count_creating.output, categorical_feature = settings.categorical_feat),
        rules.heatmap_creating.output,
        rules.pairplot_creating.output,
        rules.anomaly_df.output,
