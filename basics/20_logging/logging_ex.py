import logging

# logging.basicConfig(level=logging.INFO)

# logging.info("Program started")
# logging.warning("Something unusual happened")
# logging.error("Something went wrong")


logging.basicConfig(
    filename="app.log",
    level=logging.ERROR
)

try:
    result = 10 / 0
except Exception as error:
    logging.error("Something went wrong")
# app log gets: ERROR:root:Something went wrong


# -------------------------------------
# Custom logger:
logger = logging.getLogger(__name__)

# Where the log shoulg go:
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("app.log")

# those will those events that ones will be log to the file:
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# format the loggins (how each log should look like):
c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Attach the objects to each fomart object:
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Link them to our custom object to pass the handles:
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# Logs events to see some action:
logger.warning("This is a warning") # __main__ - WARNING - This is a warning
logger.error("This is an error")    # __main__ - WARNING - This is a warning