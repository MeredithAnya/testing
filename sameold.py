import os
import sentry_sdk

version = os.environ.get('$GITHUB_SHA', '1.0.0')

# getsentry LOCAL project
# sentry_sdk.init(dsn='https://726d59757f1f4b46852c61dff3dafc9b@meredith.ngrok.io/2', release=version)

# sentry LOCAL project:blah
sentry_sdk.init(dsn='https://8930388f5eeb4635bb3cf6739817eab7@meredith.ngrok.io/2', release=version)

# DOOM
# sentry_sdk.init(dsn='https://4c0b4d78a85e4531a128a4730cd4c70b@o49697.ingest.sentry.io/4511291', release=version)

def try_again(text):
  # not a thing
  text.enlarge()
  

try: 
   try_again('meep')
except Exception as err:
   sentry_sdk.capture_exception(err)
