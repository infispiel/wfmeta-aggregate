from argparse import ArgumentParser
from typing import Tuple
from .core import srcType

class darshan(srcType):
    skip: bool = False
    long_name:str = "Darshan"
    description:str = "Metadata collected from Darshan logs."
    argument_prefix: str = "drsh"

    @staticmethod
    def make_args(parser: ArgumentParser) -> None:
        grp = parser.add_argument_group(darshan.long_name, darshan.description)
        grp.add_argument("--drsh-ignore", action="store_true",
                            help="Do not attempt to read darshan metadata files.")
        grp.add_argument("--drsh-i", 
                            help="Input folder location for darshan metadata.")
        
    @staticmethod
    def validate_args(args) -> Tuple[bool, str]:
        if "drsh_ignore" not in args.keys() or args["drsh_ignore"] is False :
            if "drsh_i" not in args.keys() or args["drsh_i"] is None :
                return (False, "error: either drsh_ignore or drsh_i must be provided.")

        return (True, "")
    
    @staticmethod
    def should_run(args) -> bool:
        return not args["drsh_ignore"]