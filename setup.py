from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="vibe-lock",
    version="0.0.1a1",
    author="Donald Watts",
    author_email="donald@vibe-lock.dev",
    description="Vast Intelligence-Based Extraction Containment Toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Donald-Watts/VIBE-Lock",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
    install_requires=[
        "cryptography>=41.0.0",
        "gitpython>=3.1.0",
        "pyyaml>=6.0.0",
    ],
    entry_points={
        "console_scripts": [
            "vibe-init=vibe_lock.vibe_init:main",
            "vibe-stamp=vibe_lock.vibe_stamp:main",
            "vibe-scan=vibe_lock.vibe_scan:main",
        ],
    },
) 