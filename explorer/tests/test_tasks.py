from django.test import TestCase
from explorer.app_settings import EXPLORER_DEFAULT_CONNECTION as CONN
from explorer.tasks import snapshot_queries, truncate_querylogs, build_schema_cache_async
from explorer.tests.factories import SimpleQueryFactory
from django.core import mail
from unittest.mock import Mock, patch
from six import StringIO
from explorer.models import QueryLog
from datetime import datetime, timedelta


class TestTasks(TestCase):

    @patch('explorer.tasks.s3_upload')
    def test_snapshots(self, mocked_upload):
        mocked_upload.return_value = 'http://s3.com/your-file.csv'

        SimpleQueryFactory(snapshot=True)
        SimpleQueryFactory(snapshot=True)
        SimpleQueryFactory(snapshot=True)
        SimpleQueryFactory(snapshot=False)

        snapshot_queries()
        self.assertEqual(mocked_upload.call_count, 3)

    def test_truncating_querylogs(self):
        QueryLog(sql='foo').save()
        QueryLog.objects.filter(sql='foo').update(run_at=datetime.now() - timedelta(days=30))
        QueryLog(sql='bar').save()
        QueryLog.objects.filter(sql='bar').update(run_at=datetime.now() - timedelta(days=29))
        truncate_querylogs(30)
        self.assertEqual(QueryLog.objects.count(), 1)

    @patch('explorer.schema.build_schema_info')
    def test_build_schema_cache_async(self, mocked_build):
        mocked_build.return_value = ['list_of_tuples']
        schema = build_schema_cache_async(CONN)
        assert mocked_build.called
        self.assertEqual(schema, ['list_of_tuples'])
