import os, glob
from setuptools import find_packages, setup

package_name = 'python_examples'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob.glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='email',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'topic_republisher = python_examples.topic_republisher:main',
            'scan_subscriber = python_examples.scan_subscriber:main',
            'robot_manipulator = python_examples.robot_manipulator:main',
            'print_pose = python_examples.print_pose:main',
            'minimal_service_client = python_examples.minimal_service_client:main',
            'turtle_dance = python_examples.turtle_dance:main'
        ],
    },
)
