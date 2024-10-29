from setuptools import find_packages, setup

package_name = 'demo_python_pkg'

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
    maintainer='wang',
    maintainer_email='wang@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "python_node=demo_python_pkg.python_node:main",#执行demo_python_pkg功能包下的python_node文件下的main函数，并生成python_node.exe编译文件
            "person_node=demo_python_pkg.person_node:main",
            "write_node=demo_python_pkg.write_node:main",
            "learn_thread=demo_python_pkg.learn_thread:main",
        ],
    },
)
