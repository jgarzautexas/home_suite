# conftest.py
"""
Fixtures in this file are allowed accross multiple modules in the directory

"""

import pytest
# import os
# import sys

# sys.path.append(os.path.dirname(__file__))


# @pytest.fixture(scope="module")
# def request_setup(request):
#     """Returns a request wrapper object.

#     """

#     server = getattr(request.module, 'SERVER', None)
#     req_obj = simple_request.RequestObj(server=server)

#     @request.addfinalizer
#     def fin():
#         pass

#     return req_obj

# def fake_process_request(self, request):
#     """
#     Returns None Object. You can also add to request obj.
#     EX.
#         request.META['HTTP_UIN'] = "FAKEUIN"
#         request.META['HTTP_SERVICE'] = 'TEST'
#         request.META['HTTP_USER_AGENT'] = ''

#     """

#     return


# @pytest.fixture(scope="module")
# def fake_utdirect(request):
#     """Fakes the utdirect login process.
#     """
#     from mock import patch

#     patcher = patch(
#         "utdirect.middleware.HttpHeaderMiddleware.process_request",
#         fake_process_request
#     )
#     patcher.start()

#     @request.addfinalizer
#     def fin():
#         """Teardown
#         """
#         patcher.stop()

#     return 



