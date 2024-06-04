from argparse import ArgumentParser
from config import Config
from app import App
 
def main():
    """Init app load config from args and run app with bot"""
    ## parse argument for load config
    parser = ArgumentParser(description='Script so useful.')
    parser.add_argument("--config", type=str ,default='')
    args = parser.parse_args()

    ## check required field
    cfg_path = args.config
    if cfg_path == '':
        exit(print("config path required! python . --config={path}"))

    app = App(cfg_path)
    app.StartTelegramBot()

if __name__ == "__main__":
    main()