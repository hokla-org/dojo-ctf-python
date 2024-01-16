import sys
from APIService import APIService
from FileService import FileService
from FlagRetriever import FlagRetriever
import asyncio

fetch = None

if len(sys.argv) < 2:
    print("Missing argument. Expected: 'api' or 'file'")
    sys.exit(1)

arg = sys.argv[1]

if arg == "api":
    APIService.get_instance().init("1234")
    fetch = APIService.get_instance().fetch
elif arg == "file":
    fetch = FileService.get_instance().fetch
else:
    print("Wrong argument. Expected: 'api' or 'file'")
    sys.exit(1)

retriever = FlagRetriever(fetch)

async def main():
    flag = await retriever.fetch_flag()
    print(flag)

if __name__ == "__main__":
    asyncio.run(main())