from generators.base_generator import Generator


class InsertManager:
    def __init__(self, *, table_name='<your_table>', generators, db_name=None, prefix='', ending=''):
        self.generators = list(generators)
        self.table_name = table_name
        self.db_name = db_name
        self.prefix = prefix
        self.ending = ending

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
        query += ';'
        return self.prefix + '\n' + query + '\n' + self.ending



