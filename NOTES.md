# Firmware compilation etc

Bootloaders of right and left halves are different. To setup, run:

```bash
qmk config user.keyboard=lily58/left
qmk compile
qmk flash
```

or if you're compiling for the right side:

```bash
qmk config user.keyboard=lily58/right
```
