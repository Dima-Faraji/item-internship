import click
from click import Group

from ..openkapsarc import OpenKAPSARC
from . import main as _phase1

historical = Group('historical', help="Manipulate the historical database.")


@historical.command()
@click.argument('server', default=None, required=False)
def demo(server):
    """Access the KAPSARC APIs at the given SERVER."""
    ok = OpenKAPSARC(server)

    print('List of all datasets:')
    for ds in ok.datasets():
        print(ds)

    print("\n\nDatasets with the 'iTEM' keyword:")
    for ds in ok.datasets(kw='item'):
        print(ds)

    print('\n\nData from one table in a branch in a repository:')
    print(ok.table('modal-split-of-freight-transport'))


@historical.command()
@click.argument('output_file', type=click.Path(dir_okay=False, writable=True),
                default='IK2_Open_Data_conv_phase1.csv')
@click.option('--use-cache/--no-cache', is_flag=True, default=True,
              help='Use cached files (no network traffic).')
def phase1(output_file, use_cache):
    """Convert raw data to have consistent columns and units.

    OUTPUT_FILE defaults to 'IK2_Open_Data_conv_phase1.csv'.
    """
    _phase1(output_file, use_cache)