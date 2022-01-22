class Callback():
    def ready_callback(current_user):
        print(f"Our user: {current_user}")

    def disconnected_callback(codeno, codemsg):
        print("Disconnected from Discord rich presence RPC.", end=" ")
        print(f"Code {codeno}: {codemsg}")

    def error_callback(errno, errmsg):
        print(f"An error occurred! Error {errno}: {errmsg}")

    @classmethod
    def get_callbacks(cls):
        return {
            "ready": cls.ready_callback,
            "disconnected": cls.disconnected_callback,
            "error": cls.error_callback,
        }
