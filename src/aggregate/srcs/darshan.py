from argparse import ArgumentParser
from .core import srcTemplate

class darshan(srcTemplate):
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
    def validate_args(args) -> bool:
        if "drsh_ignore" not in args.keys() or args["drsh_ignore"] is False :
            if "drsh_i" not in args.keys() or args["drsh_i"] is None :
                return False

        return True