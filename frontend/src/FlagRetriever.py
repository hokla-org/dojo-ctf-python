class FlagRetriever:
    def __init__(self, fetch_fn):
        self.fetch_fn = fetch_fn

    async def fetch_flag(self):
        response = await self.fetch_fn("flag")
        return response
