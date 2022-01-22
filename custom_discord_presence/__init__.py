from custom_discord_presence.callbacks import Callback
import discord_rpc
import time


def setup_discord_rpc(app_id):
    discord_rpc.initialize(
        app_id=app_id,
        callbacks=Callback.get_callbacks(),
        log=False
    )


def execute_custom_presence(app_id, description, image):
    try:

        setup_discord_rpc(app_id)
        start = time.time()

        while True:
            discord_rpc.update_presence(
                details=description,
                start_timestamp=start,
                large_image_key=image
            )

            discord_rpc.update_connection()

            time.sleep(2)

            discord_rpc.run_callbacks()

    except KeyboardInterrupt:
        discord_rpc.shutdown()
