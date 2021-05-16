import click
from bt_excel_cli import excel
import os

@click.group()
def main():
    pass

@click.command('create')
def create():
    click.echo("Creates new records and adds to excel")


@click.command('retrieve')
@click.option('--location', '-l', help="Location", required=True, type=str)
@click.option('--directory', '-d', help="Directory Name", required=True, type=str)
@click.option('--filename', '-f', help="File Name", required=True, type=str)
@click.option('--sheetname', '-s', help="Sheet Name", required=True, type=str)
def retrieve(location, directory, filename, sheetname):
    click.echo("retrieveing all records in spreadsheet")
    data = excel.Excel(
        location, directory, filename, sheetname)
    records = data.retrieve_records(sheet_name=sheetname)
    print(records)
    

@click.command('limited')
@click.option('--location', '-l', help="Location", required=True, type=str)
@click.option('--directory', '-d', help="Directory Name", required=True, type=str)
@click.option('--filename', '-f', help="File Name", required=True, type=str)
@click.option('--sheetname', '-s', help="Sheet Name", required=True, type=str)
@click.option('--numrows', '-n', help="Number of Rows", required=True, type=int)
def limited(location, directory, filename, sheetname, numrows):
    click.echo("retrieveing limited records in spreadsheet")
    data = excel.Excel(
        location, directory, filename, sheetname)
    limit_records = data.retrieve_limited_records(
            sheet_name=sheetname, number_of_rows_retrieved=numrows)
    print(limit_records)


@click.command('retrieve_condition')
@click.option('--location', '-l', help="Location", required=True, type=str)
@click.option('--directory', '-d', help="Directory Name", required=True, type=str)
@click.option('--filename', '-f', help="File Name", required=True, type=str)
@click.option('--sheetname', '-s', help="Sheet Name", required=True, type=str)
@click.option('--condition', '-c', help="Condition", required=True)
def retrieve_condition(location, directory, filename, sheetname, **condition):
    click.echo("retrieveing records by condition from spreadsheet")
    data = excel.Excel(
        location, directory, filename, sheetname)
    condition_records = data.retrieve_records_by_condition(
        sheet_name=sheetname, condition=condition)
    print(condition_records)

@click.command('update')
def update():
    click.echo("updates records in excel")


@click.command('delete')
def delete():
    click.echo("deletes records in excel")


@click.command('bulk')
def bulk():
    click.echo("bulk changes in excel")


main.add_command(create)
main.add_command(retrieve)
main.add_command(retrieve_condition)
main.add_command(limited)
main.add_command(update)
main.add_command(delete)
main.add_command(bulk)

if __name__ == '__main__':
    main()
