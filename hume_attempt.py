import asyncio
import json

from hume import HumeStreamClient
from hume.models.config import LanguageConfig

with open('emojis_sample.json', 'r', encoding="utf-8") as f:
    data = json.load(f)
    
samples = [
    "Mary had a little lamb,",
    "Its fleece was white as snow."
    "Everywhere the child went,"
    "The little lamb was sure to go."
]

# print(data)

async def main():
    client = HumeStreamClient("QUANHZQQ2VRBSixAhGfNvsDGCWuGu5TnUk03l5S2lukw32sI")
    config = LanguageConfig()
    async with client.connect([config]) as socket:
        for point in data['emojis_sample']:
            result = await socket.send_text(point['name'])
            predictions = result["language"]["predictions"]
            res = []
            dic = {}
            for i in range(predictions['emotions']['name']):
                dic[i] = 0
            for word in predictions:
                emotions = word["emotions"]
                dic[emotions['name']] += emotions['score']
            top_emotions = sorted(dic.values, reverse=True)[:5]
            print(point['name'] + top_emotions)

asyncio.run(main())

# so in order to embed the data, I need to take all the text, take the top 5 detected emotions, and put them on a multidimentional vector
# once the emoji vectors are embed, then use website to take audio input 

