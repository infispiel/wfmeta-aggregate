import argparse as ap
from typing import Tuple

class srcType:
    skip: bool = True
    long_name: str
    description: str
    argument_prefix: str
    verbose: bool

    @staticmethod
    def make_args(parser: ap.ArgumentParser) -> None :
        raise NotImplementedError
    
    @staticmethod
    def validate_args(args) -> Tuple[bool, str]:
        raise NotImplementedError
    
    @staticmethod
    def should_run(args) -> bool:
        raise NotImplementedError
    
    def __init__(self, args):
        raise NotImplementedError