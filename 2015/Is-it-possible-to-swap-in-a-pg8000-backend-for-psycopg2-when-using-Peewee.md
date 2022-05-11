# Is it possible to swap in a pg8000 backend for psycopg2 when using Peewee?

	author: Steve Theodore
	written: 2015-06-05
	views: 928
	upvotes: 0
	quora url: /Is-it-possible-to-swap-in-a-pg8000-backend-for-psycopg2-when-using-Peewee/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


This appears to work, though I haven't really put it through it's paces yet



    from peewee import Database, ColumnMetadata, ForeignKeyMetadata, IndexMetadata, OP
    
    class PG8000Database(Database):
     commit_select = True
     compound_select_parentheses = True
     distinct_on = True
     drop_cascade = True
     field_overrides = {
     'blob': 'BYTEA',
     'bool': 'BOOLEAN',
     'datetime': 'TIMESTAMP',
     'decimal': 'NUMERIC',
     'double': 'DOUBLE PRECISION',
     'primary_key': 'SERIAL',
     'uuid': 'UUID',
     }
     for_update = True
     for_update_nowait = True
     insert_returning = True
     interpolation = '%s'
     op_overrides = {
     OP.REGEXP: '~',
     }
     reserved_tables = ['user']
     sequences = True
     window_functions = True
    
     register_unicode = True
    
     def _connect(self, database, encoding='utf-8', **kwargs):
     conn = pg8000.connect(database=database, **kwargs)
     return conn
    
     def _get_pk_sequence(self, model):
     meta = model._meta
     if meta.primary_key.sequence:
     return meta.primary_key.sequence
     elif meta.auto_increment:
     return '%s_%s_seq' % (meta.db_table, meta.primary_key.db_column)
    
     def last_insert_id(self, cursor, model):
     sequence = self._get_pk_sequence(model)
     if not sequence:
     return
    
     meta = model._meta
     if meta.schema:
     schema = '%s.' % meta.schema
     else:
     schema = ''
    
     cursor.execute("SELECT CURRVAL('%s\"%s\"')" % (schema, sequence))
     result = cursor.fetchone()[0]
     if self.get_autocommit():
     self.commit()
     return result
    
     def get_tables(self, schema='public'):
     query = ('SELECT tablename FROM pg_catalog.pg_tables '
     'WHERE schemaname = %s ORDER BY tablename')
     return [r for r, in self.execute_sql(query, (schema,)).fetchall()]
    
     def get_indexes(self, table, schema='public'):
     query = """
     SELECT
     i.relname, idxs.indexdef, idx.indisunique,
     array_to_string(array_agg(cols.attname), ',')
     FROM pg_catalog.pg_class AS t
     INNER JOIN pg_catalog.pg_index AS idx ON t.oid = idx.indrelid
     INNER JOIN pg_catalog.pg_class AS i ON idx.indexrelid = i.oid
     INNER JOIN pg_catalog.pg_indexes AS idxs ON
     (idxs.tablename = t.relname AND idxs.indexname = i.relname)
     LEFT OUTER JOIN pg_catalog.pg_attribute AS cols ON
     (cols.attrelid = t.oid AND cols.attnum = ANY(idx.indkey))
     WHERE t.relname = %s AND t.relkind = %s AND idxs.schemaname = %s
     GROUP BY i.relname, idxs.indexdef, idx.indisunique
     ORDER BY idx.indisunique DESC, i.relname;"""
     cursor = self.execute_sql(query, (table, 'r', schema))
     return [IndexMetadata(row[0], row[1], row[3].split(','), row[2], table)
     for row in cursor.fetchall()]
    
     def get_columns(self, table, schema='public'):
     query = """
     SELECT column_name, is_nullable, data_type
     FROM information_schema.columns
     WHERE table_name = %s AND table_schema = %s
     ORDER BY ordinal_position"""
     cursor = self.execute_sql(query, (table, schema))
     pks = set(self.get_primary_keys(table, schema))
     return [ColumnMetadata(name, dt, null == 'YES', name in pks, table)
     for name, null, dt in cursor.fetchall()]
    
     def get_primary_keys(self, table, schema='public'):
     query = """
     SELECT kc.column_name
     FROM information_schema.table_constraints AS tc
     INNER JOIN information_schema.key_column_usage AS kc ON (
     tc.table_name = kc.table_name AND
     tc.table_schema = kc.table_schema AND
     tc.constraint_name = kc.constraint_name)
     WHERE
     tc.constraint_type = %s AND
     tc.table_name = %s AND
     tc.table_schema = %s"""
     cursor = self.execute_sql(query, ('PRIMARY KEY', table, schema))
     return [row for row, in cursor.fetchall()]
    
     def get_foreign_keys(self, table, schema='public'):
     sql = """
     SELECT
     kcu.column_name, ccu.table_name, ccu.column_name
     FROM information_schema.table_constraints AS tc
     JOIN information_schema.key_column_usage AS kcu
     ON (tc.constraint_name = kcu.constraint_name AND
     tc.constraint_schema = kcu.constraint_schema)
     JOIN information_schema.constraint_column_usage AS ccu
     ON (ccu.constraint_name = tc.constraint_name AND
     ccu.constraint_schema = tc.constraint_schema)
     WHERE
     tc.constraint_type = 'FOREIGN KEY' AND
     tc.table_name = %s AND
     tc.table_schema = %s"""
     cursor = self.execute_sql(sql, (table, schema))
     return [ForeignKeyMetadata(row[0], row[1], row[2], table)
     for row in cursor.fetchall()]
    
     def sequence_exists(self, sequence):
     res = self.execute_sql("""
     SELECT COUNT(*) FROM pg_class, pg_namespace
     WHERE relkind='S'
     AND pg_class.relnamespace = pg_namespace.oid
     AND relname=%s""", (sequence,))
     return bool(res.fetchone()[0])
    
     def set_search_path(self, *search_path):
     path_params = ','.join(['%s'] * len(search_path))
     self.execute_sql('SET search_path TO %s' % path_params, search_path)



I did run into this when I tried running a peewee query and slicing the result:

[pg8000.errors.ProgrammingError: ('ERROR', '34000', 'portal "pg8000_portal_1" does not exist') · Issue #39 · mfenniak/pg8000](https://github.com/mfenniak/pg8000/issues/39)

However that's really user error: I should have either subsetted the query on the server or used itertools.islice() on the results

