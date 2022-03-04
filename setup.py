import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="signal_backtester",
    version="1.0.4",
    author="Ali moradi",
    author_email="ali.mrd318@gmail.com",
    description="tiny library for fast backtest on generated signals",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xibalbas/signal_backtester",
    project_urls={
        "Bug Tracker": "https://github.com/xibalbas/signal_backtester/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires = [
        'backtesting',
        'pydantic'
        ],
    python_requires=">=3.7",
)