from django.conf.urls import url

from explorer.views import (
    ConnectionBrowserListView,
    CreateQueryView,
    DeleteQueryView,
    DownloadFromSqlView,
    DownloadQueryView,
    format_sql,
    ListQueryLogView,
    ListQueryView,
    PlayQueryView,
    QueryView,
    SchemaView,
    StreamQueryView,
    TableBrowserDetailView,
    TableBrowserListView,
)

urlpatterns = [
    url(r'(?P<query_id>\d+)/$', QueryView.as_view(), name='query_detail'),
    url(r'(?P<query_id>\d+)/download$', DownloadQueryView.as_view(), name='download_query'),
    url(r'(?P<query_id>\d+)/stream$', StreamQueryView.as_view(), name='stream_query'),
    url(r'download$', DownloadFromSqlView.as_view(), name='download_sql'),
    url(r'(?P<pk>\d+)/delete$', DeleteQueryView.as_view(), name='query_delete'),
    url(r'new/$', CreateQueryView.as_view(), name='query_create'),
    url(r'play/$', PlayQueryView.as_view(), name='explorer_playground'),
    url(r'schema/(?P<connection>.+)$', SchemaView.as_view(), name='explorer_schema'),
    url(r'logs/$', ListQueryLogView.as_view(), name='explorer_logs'),
    url(r'format/$', format_sql, name='format_sql'),
    url(r'^$', ListQueryView.as_view(), name='explorer_index'),
    url(r'browse/$', ConnectionBrowserListView.as_view(), name='connection_browser_list'),
    url(r'browse/(?P<connection>.+)/$', TableBrowserListView.as_view(), name='table_browser_list'),
    url(
        r'browse/(?P<connection>.+)/(?P<schema>.+)/(?P<table>.+)$',
        TableBrowserDetailView.as_view(),
        name='table_browser_detail',
    ),
]
