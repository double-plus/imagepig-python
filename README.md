# imagepig
Python package for [Image Pig](https://imagepig.com/), the API for AI images.

Example of basic usage:

```python
from imagepig import ImagePig

# create instance of API (put here your actual API key)
imagepig = ImagePig("your-api-key")

# call the API with a prompt to generate an image
result = imagepig.xl("cute piglet running on a green garden")

# save image to a file
result.save('cute-piglet.jpeg')

# or access image data (bytes)
result.data

# or access image as an object (needs to have the Pillow package installed)
result.image
```
