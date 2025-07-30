import argparse as ap

class srcTemplate:
    long_name: str
    description: str
    argument_prefix: str

    @staticmethod
    def make_args(parser: ap.ArgumentParser) -> None :
        raise NotImplementedError
    
    @staticmethod
    def validate_args(args) -> bool:
        raise NotImplementedError