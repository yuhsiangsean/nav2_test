from setuptools import find_packages, setup

package_name = 'nav2_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='a0929370607@gmail.com',
    description=(
        'Test rig for isolating the map-frame goal-point mismatch: '
        'same state machine as single_uav_hover, plus commands 5/6 '
        'to fly straight to absolute (0.5,0)/(0,0.5) targets without '
        'going through Nav2.'
    ),
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'nav2_test_control = nav2_test.nav2_test_control:main',
            'nav2_test_commander = nav2_test.nav2_test_commander:main',
        ],
    },
)
