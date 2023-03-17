import click
from nbparameterise import extract_parameters, parameter_values, replace_definitions
from nbclient import execute
import nbformat
import subprocess

@click.command() 
@click.option("-c", "--path_config", help="Path to config yml to use")
@click.option("-n", "--output_name", help="Name of new executed and exported nb")
def main(path_config, output_name):
    nb = nbformat.read("module_04.ipynb", as_version=4)
    orig_parameters = extract_parameters(nb)
    params = parameter_values(orig_parameters, config_path=path_config)
    new_nb = replace_definitions(nb, params)
    
    # run
    execute(new_nb)

    # Save
    with open(f"{output_name}.ipynb", 'w') as f:
        nbformat.write(new_nb, f)
    
    # export
    subprocess.call([
    'jupyter',
    'nbconvert',
    '--no-input',
    '--to', 'html_embed',
    '--template', 'toc2',
    f'{output_name}.ipynb'])
    
if __name__ == '__main__':
    main()
