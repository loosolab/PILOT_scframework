from setuptools import find_packages, setup

setup(
    name='pilotpy',
    version='2.0.6',
    author='Mehdi Joodaki',
    author_email='judakimehdi@gmail.com',
    url='https://github.com/dlnija/PILOT_fork',
    install_requires=[
            "cycler",
            "joypy",
            "leidenalg",
            "numpy",
            "matplotlib",
            "pandas",
            "plotly",
            "plotnine",
            "pot",
            "pydiffmap",
            "scanpy",
            "scikit-learn",
            "scikit-network",
            "scipy",
            "seaborn",
            "shap",
            "statsmodels",
            "elpigraph-python",
            "adjusttext",
            "gprofiler-official",
            "gseapy"
        ],
        packages=find_packages()
)

