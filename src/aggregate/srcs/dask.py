from argparse import ArgumentParser
from .core import srcTemplate

class dask(srcTemplate):
    long_name: str = "DASK"
    description: str = "Metadata collected from the DASK workflow definition language."
    argument_prefix: str = "dask"

    @staticmethod
    def make_args(parser: ArgumentParser) -> None:
        grp = parser.add_argument_group(dask.long_name, dask.description)
        grp.add_argument("--dask-ignore", action="store_true",
                            help="Do not attempt to read DASK metadata files.")
        grp.add_argument("--dask-i", 
                            help="Input folder location for DASK metadata.")
        
    @staticmethod
    def validate_args(args) -> bool:
        if "dask_ignore" not in args.keys() or args["dask_ignore"] is None :
            if "dask_i" not in args.keys() or args["dask_i"] is None :
                return False

        return True