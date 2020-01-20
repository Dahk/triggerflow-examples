#!/usr/bin/env python3
import click
import json
import dags.client as client


@click.group()
@click.pass_context
def cli(ctx):
    pass


@cli.command('make')
@click.argument('dag_path')
@click.option('--output', '-o', help='Resulting dag in json format', type=str)
def cli_make(dag_path, output):
    dag_json = client.make(dag_path)
    if output is None:
        print(dag_json)
    else:
        with open(output, 'w') as dagf:
            dagf.write(dag_json)


@cli.command('deploy')
@click.argument('dag_json', type=click.File('r'))
def cli_deploy(dag_json):
    client.deploy(json.loads(dag_json.read()))


@cli.command('run')
@click.argument('dagrun_id', type=str)
def cli_run(dagrun_id):
    status_code, res = client.run(dag_id)
    print('{} {}'.format(status_code, res))


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter