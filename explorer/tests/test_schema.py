from unittest.mock import patch

from django.test import TestCase

from explorer import schema
from explorer.app_settings import EXPLORER_CONNECTIONS


class TestSchemaInfo(TestCase):
    databases = ['postgres']

    @patch('explorer.schema._get_includes')
    @patch('explorer.schema._get_excludes')
    def test_schema_info_returns_valid_data(self, mocked_excludes, mocked_includes):
        mocked_includes.return_value = None
        mocked_excludes.return_value = []
        res = schema.schema_info(EXPLORER_CONNECTIONS['Postgres'])
        assert mocked_includes.called  # sanity check: ensure patch worked
        tables = [x.name.name for x in res]
        self.assertIn('explorer_query', tables)
        schemas = [x.name.schema for x in res]
        self.assertIn('public', schemas)

    @patch('explorer.schema._get_includes')
    @patch('explorer.schema._get_excludes')
    def test_table_exclusion_list(self, mocked_excludes, mocked_includes):
        mocked_includes.return_value = None
        mocked_excludes.return_value = ('explorer_',)
        res = schema.schema_info(EXPLORER_CONNECTIONS['Postgres'])
        tables = [x.name.name for x in res]
        self.assertNotIn('explorer_query', tables)

    @patch('explorer.schema._get_includes')
    @patch('explorer.schema._get_excludes')
    def test_app_inclusion_list(self, mocked_excludes, mocked_includes):
        mocked_includes.return_value = ('auth_',)
        mocked_excludes.return_value = []
        res = schema.schema_info(EXPLORER_CONNECTIONS['Postgres'])
        tables = [x.name.name for x in res]
        self.assertNotIn('explorer_query', tables)
        self.assertIn('auth_user', tables)

    @patch('explorer.schema._get_includes')
    @patch('explorer.schema._get_excludes')
    def test_app_inclusion_list_excluded(self, mocked_excludes, mocked_includes):
        # Inclusion list "wins"
        mocked_includes.return_value = ('explorer_',)
        mocked_excludes.return_value = ('explorer_',)
        res = schema.schema_info(EXPLORER_CONNECTIONS['Postgres'])
        tables = [x.name.name for x in res]
        self.assertIn('explorer_query', tables)

    @patch('explorer.schema.do_async')
    def test_builds_async(self, mocked_async_check):
        mocked_async_check.return_value = True
        self.assertIsNone(schema.schema_info(EXPLORER_CONNECTIONS['Postgres']))
