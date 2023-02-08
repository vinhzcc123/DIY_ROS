from setuptools import setup

package_name = 'ros2_demo_py'

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
    maintainer='vinhnq36',
    maintainer_email='vinhnq36@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "first_node = ros2_demo_py.my_first_py:main",
            "robot_news_station = ros2_demo_py.robot_news_station:main",
            "smartphone = ros2_demo_py.smartphone:main",
            "add_two_ints_server = ros2_demo_py.add_two_ints_server:main",
            "add_two_ints_client = ros2_demo_py.add_two_ints_client:main",
            "hw_status_publisher = ros2_demo_py.hw_status_publisher:main",
            "led_panel = ros2_demo_py.led_panel:main",
            "battery = ros2_demo_py.battery:main",
            "face-detect_server = ros2_demo_py.detect_faces_server:main",
            "face-detect_client = ros2_demo_py.face_detect_client:main"
        ],
    },
)
