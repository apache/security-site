import asyncio
import ahapi.session

httpserver = ahapi.simple(
    api_dir="app/scripts",  # serve api end points from here
    static_dir="app/htdocs",  # serve stuff like html and images from here
    bind_ip="127.0.0.1",
    bind_port="8082",
    log_stdout=True,
)

asyncio.run(httpserver.loop())
