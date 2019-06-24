name = 'maya'

version = '2018.6.0'

variants = [
    ['platform-windows', 'arch-AMD64']
]


def commands():
    env.MAYA_LOCATION = '{root}'
