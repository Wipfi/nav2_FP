from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ais_nav2_fp_tutorial'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch*')),
        (os.path.join('share', package_name, 'config'), glob('config/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Facundo Garcia',
    maintainer_email='facundo.garcia@fixposition.com',
    description='GPS Waypoints Follower for AgileX Scout Mini',
    license='MIT',
    tests_require=['pytest']
)
