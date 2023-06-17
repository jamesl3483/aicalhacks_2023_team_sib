from hume import HumeBatchClient
from hume.models.config import FaceConfig

client = HumeBatchClient("QUANHZQQ2VRBSixAhGfNvsDGCWuGu5TnUk03l5S2lukw32sI")
urls = ["https://iep.utm.edu/wp-content/media/hume-bust.jpg"]
config = FaceConfig()
job = client.submit_job(urls, [config])