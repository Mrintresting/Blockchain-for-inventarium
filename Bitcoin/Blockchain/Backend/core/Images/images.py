from PIL import Image
from PIL.ExifTags import TAGS
import json
from pathlib import Path

#C:\Users\work\OneDrive\Desktop\Bitcoin\Blockchain\Backend\core\Images\Images_from_camera\photo.jpg
class images:
    def __init__(self,image_path):
        self.image_path=image_path

    def extract_metadata(self):

        image = Image.open(self.image_path)
        exif_data = image._getexif()
    
        metadata = {}
        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                metadata[tag] = value
    

        cleaned = {}
        for key, value in metadata.items():
            if isinstance(value, bytes):
                cleaned[key] = value.hex()   # convert bytes → hex string
            else:
                cleaned[key] = value
        return cleaned
    



'''path= Path("C:\\Users\\work\\OneDrive\\Desktop\\Bitcoin\\Images\\Signature.jpg")


metadata = images(path).extract_metadata()
print(metadata)'''