# Gamma

### A simple ECS game engine for Python, built on Pygame, with an emphasis on ease of use.

## Installing

```
python3 setup.py install
```

Note: This library is currently in early development. Until it reaches version 1.0 it will change a lot, including the introduction of some breaking changes.

Until the library is more stable, it's advised to install using `python3 setup.py develop` in a virtual environment. This means that changes made to the library won't require a reinstall. Just `git pull` to get the latest version.

```
pip3 install virtualenv
virtualenv venv
python3 setup.py develop
source venv/bin/activate
```

## Changelog

|Version|Description|
|---|---|
|0.1|Initial engine version. Includes a basic ECS implementation, scenes (and transitions) and some UI elements. There are very basic versions of a number of systems.|
|0.2|Some improvements to the systems, mainly adding optional parameters to allow customisation.|
|0.3|More improvements to the systems, including the addition of a renderer for each scene. This takes the drawing away from the camera system, and allows for the addition of custom systems that can draw.|

## Licence

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.