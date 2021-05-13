import click

@click.group()
def main():
    pass

@click.command('create')
def create():
    click.echo("Creates new records and adds to excel")


@click.command('retrieve')
def retrieve():
    click.echo("retrieves records from excel")


@click.command('update')
def update():
    click.echo("updates records in excel")


@click.command('delete')
def delete():
    click.echo("deletes records in excel")


main.add_command(create)
main.add_command(retrieve)
main.add_command(update)
main.add_command(delete)

if __name__ == '__main__':
    main()
