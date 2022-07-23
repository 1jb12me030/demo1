from rest_framework.pagination import CursorPagination
from rest_framework import pagination

class CustomPageNumberPageination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = "records"
    max_page_size = 5
    page_query_param = 'p'

class CursorPaginationWithOrdering(CursorPagination):
    # order based on id
    ordering = 'id'