from setuptools import setup

package_name = 'my_py_pkg'

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
    maintainer='sharath',
    maintainer_email='returncode13@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = my_py_pkg.my_first_node:main", #name (py_node here) for the executable 
                                                     #to be placed in the "install" folder
            "robot_news_station = my_py_pkg.robot_news_station:main",   #robot news station executable 
            "smartphone = my_py_pkg.smartphone:main", #smartphone subscriber executable
            "add_two_ints_server= my_py_pkg.add_two_ints_server:main", #add_two_ints_server service executable
            "add_two_ints_client_no_oop = my_py_pkg.add_two_ints_client_no_oop:main" #add_two_ints_client_no_oop executable
        ],
    },
)
