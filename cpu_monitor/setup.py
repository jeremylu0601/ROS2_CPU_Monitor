from setuptools import setup

package_name = 'cpu_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='YourName',
    maintainer_email='you@email.com',
    description='display the usage of CPU',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'monitor = cpu_monitor.monitor:main',
            'monitor_individual = cpu_monitor.monitor_individual:main',
        ],
    },
)
