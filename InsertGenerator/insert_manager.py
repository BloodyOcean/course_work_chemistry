from generators.base_generator import Generator


class SQLServerInsertManager:
    def __init__(self, generators, table_name='<your_table>', db_name=None, *, prefix=''):
        self.generators = list(generators)
        self.table_name = table_name
        self.db_name = db_name
        self.prefix = prefix

    def get_insert_query(self, rows: int):
        query = f'USE [{self.db_name}]\n' if self.db_name else ''
        query += f'INSERT INTO [{self.table_name}] VALUES\n'
        for row in range(rows):
            query += '('
            for gen in self.generators:
                query += gen.next()
                if gen != self.generators[-1]:
                    query += ', '
            query += ')'
            if row != rows - 1:
                query += ',\n'
        return f'{self.prefix}\n{query};\nGO'



