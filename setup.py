from setuptools import setup

setup(
    name='akttym',
    version='0.1.4',
    package_data={
        'akttym': ['config.yaml']
    },
    description='Add currently plaing track by Spotify to your music library, headlessly',
    packages=['akttym'],
    entry_points={
        'console_scripts': [
            'akttym = akttym.__main__:main'
        ]
    },
    install_requires=[
        'pyyaml',
        'spotipy'
    ],
    dependency_links=[
        "git+https://github.com/plamere/spotipy.git@4c2c1d763a3653aa225c4af848409ec31286a6bf#egg=spotipy=2.4.4"
    ]
)
