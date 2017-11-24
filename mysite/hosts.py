from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'blog', settings.ROOT_URLCONF, name='blog'),
    host(r'(?!www).*', 'mysite.hostsconf.urls', name='wildcard'),
    # host(r'(\w+)', 'path.to.custom_urls', name='wildcard'),
)

'''
from mysite.hostsconf import urls as redirect_urls
host_patterns = [
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', redirect_urls, name='wildcard'),
]
'''