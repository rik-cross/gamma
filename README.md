# Gamma

![Gamma](src/gamma/images/gamma.png)

### A simple ECS game engine for Python, built on Pygame, with an emphasis on ease of use.

### Usage

- Install: `pip install pygame-gamma` or 
- Install from local source: `pip install -e [repo path]`

[Add suggestions and bugs here](https://github.com/rik-cross/gamma/issues)!

Note: This engine is currently in early development. Until it reaches version 1.0 it will change a lot, including the introduction of some breaking changes.

### Getting started

+ See the [examples](./examples/)
+ See the [Collect the Coins](./examples/collect_the_coins) example

### Changelog

|Version|Description|
|---|---|
|0.1|Initial engine version. Includes a basic ECS implementation, scenes (and transitions) and some UI elements. There are very basic versions of a number of systems.|
|0.2|Some improvements to the systems, mainly adding optional parameters to allow customisation.|
|0.3|More improvements to the systems, including the addition of a renderer for each scene. This takes the drawing away from the camera system, and allows for the addition of custom systems that can draw.|
|0.4|The addition of a 'collect the coins' example, showing how to create a very simple but complete game. This coincides with the creation of an initial video tutorial series. There are also other various edits and improvements.|

### Licence

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
