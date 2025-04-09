from setuptools import setup, find_packages

setup(
    name="phyloalignx",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyYAML",
    ],
    entry_points={
        "console_scripts": [
            "phyloalignx=msa_raxml:main",
        ],
    },
    author="Abul Khayer",
    description="A pipeline for MSA (MAFFT) and phylogenetic tree generation (RAxML)",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
