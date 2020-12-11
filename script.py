import os
import sentry_sdk

sentry_sdk.init(dsn='https://8930388f5eeb4635bb3cf6739817eab7@meredith.ngrok.io/2', release='1')

try: 
   oppydooop()
except Exception as err:
   sentry_sdk.capture_exception(err)
