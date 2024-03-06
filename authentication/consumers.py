from channels.generic.websocket import AsyncWebsocketConsumer
import json


class AsyncNotification(AsyncWebsocketConsumer):
    async def connect(self):
        self.groupname ='notification'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, code):
        return await super().disconnect(code)

    async def receive(self, text_data=None, bytes_data=None):
        return await super().receive(text_data, bytes_data)    