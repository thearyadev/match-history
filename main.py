from prisma import Prisma
from prisma.models import User

from robyn import Robyn
from robyn.templating import JinjaTemplate

app = Robyn(__file__)
prisma = Prisma(auto_register=True)

@app.startup_handler
async def startup_handler() -> None:
    await prisma.connect()


@app.shutdown_handler
async def shutdown_handler() -> None:
    if prisma.is_connected():
        await prisma.disconnect()


# @app.get("/")
# async def h():
#     user = await User.prisma().create(
#         data={
#             "name": "Robert",
#         },
#     )
#     return user.json()

@app.get("/")
async def h():
    return JinjaTemplate("public").render_template("index.html")

@app.get("/vendor/htmx.min.js")
async def htmx():
    return JinjaTemplate("public").render_template("vendor/htmx.min.js")


@app.get("/js/index.js")
async def js():
    return JinjaTemplate("public").render_template("js/index.js")

@app.get("/css/style.css")
async def css():
    return JinjaTemplate("public").render_template("css/style.css")

if __name__ == "__main__":
    app.start(host="0.0.0.0", port=8080)
