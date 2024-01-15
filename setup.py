from setuptools import setup

setup(
    name="bing-service",
    version="0.0.1",
    description="Library to bing",
    package_dir={"": "src"},
    install_requires=[
        "fastapi", 
        "uvicorn", 
        "re_edge_gpt"
    ]
)
