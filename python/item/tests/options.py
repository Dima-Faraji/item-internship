def pytest_addoption(parser):
    parser.addoption('--run-slow', action='store_true', default=False,
                     help='run slow tests')
    parser.addoption('--local-data',
                     help='path to local data for testing')
    parser.addoption('--stats-server', default='https://0.0.0.0:8080',
                     help='address of statistics server')