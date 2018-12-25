import setuptools

setuptools.setup(
        author="Filip Mroz",
        author_email="fafafft@gmail.com",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.5"
        ],
        cmdclass={},
        include_package_data=True,
        install_requires=["psutil", "elevate"],
        keywords=["freeze","memory","paging", "kill", "recover"],
        license="MIT",
        long_description="Guardians of the memory stand between you and very dark and grim times, where life is lost, despair spreads like a disease and basically you have to redo all unsaved work.",
        name="gotm",
        description="Guardians of the Memory defend Windows against its many foes, including imageio.volread()."),
        setup_requires=[],
        url="https://github.com/Fafa87/GuardiansOfTheMemory",
        version="1.0"
)
