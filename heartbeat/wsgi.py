import os
import heartbeat

port = int(os.getenv("HEARTBEAT_PORT", 5000)) #pylint: disable=invalid-name
env = os.getenv("HEARTBEAT_ENV", "production") #pylint: disable=invalid-name
environment = heartbeat.Environment.from_string(env) #pylint: disable=invalid-name
app = heartbeat.create_app(environment) #pylint: disable=invalid-name

if __name__ == "__main__":
    app.run(port=port)
