from flytekit import (
    ImageSpec,
)

image_spec = ImageSpec(
    name='classifier',
    requirements='requirements.txt',
    registry='gchr.io/cybersamx/classifier',
    base_image='ghcr.io/flyteorg/flytekit:py3.11-latest',
)
