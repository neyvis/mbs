
from django.utils.six import BytesIO

from PIL import Image


def create_image(size=(100, 100), image_mode='RGB', image_format='PNG'):
   """
   Generate a test image, returning the filename that it was saved as.

   If ``storage`` is ``None``, the BytesIO containing the image data
   will be passed instead.
   """
   data = BytesIO()
   Image.new(image_mode, size).save(data, image_format)
   data.seek(0)
   return data
