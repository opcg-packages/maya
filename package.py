name = 'maya'

version = '2019.1.0'

variants = [
    ['platform-windows', 'arch-AMD64']
]


def commands():
    env.MAYA_LOCATION = '{root}'
