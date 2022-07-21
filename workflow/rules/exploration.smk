from config import raw_path, interim_path, processed_path, reports_path, cli_path, categorical_feat, numerical_feat

rule info_extracting:
    input: 
        raw_path
    output:
        reports_path
    params:
        cli=cli_path
    shell: 
        "python {params.cli} total-info {input} {output}"

rule all_info_extracting:
    input:
        rules.info_extracting.output



