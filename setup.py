from setuptools import setup

setup(
    name='akttym',
    version='1.0.2',
    package_data={
        'akttym': ['config.yaml']
    },
    description='`Akttym` is a simple script placing heart/like/whatever-they-call-it on currently playing track on Spotify, which combined with global keyboard shortcut allows for complete headless setup.',
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    packages=['akttym'],
    entry_points={
        'console_scripts': [
            'akttym = akttym.__main__:main'
        ]
    },
    install_requires=[
        'pyyaml==5.3.1',
        'spotipy==2.11.1'
    ],
)
