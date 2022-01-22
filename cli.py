from argparse import ArgumentParser
from custom_discord_presence import execute_custom_presence


def setup_cli_parser():
    cli_description = "A simple CLI to configure discord rich presence"
    parser = ArgumentParser(description=cli_description)

    parser.add_argument("--app-id", required=True, help="Setup Discord app-id")

    parser.add_argument(
        "--description",
        required=True,
        help="Text that will be displayed"
    )

    parser.add_argument("--image", required=False, help="Image name")

    return parser.parse_args()


def run_discord_presence(args):
    app_id = args.app_id
    description = args.description
    image = args.image if args.image else "default"

    execute_custom_presence(app_id, description, image)


if __name__ == "__main__":
    args = setup_cli_parser()
    run_discord_presence(args)
