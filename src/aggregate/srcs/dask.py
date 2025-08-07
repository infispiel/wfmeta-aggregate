from argparse import ArgumentParser
from typing import Tuple
from pathlib import Path

from .core import srcType

class dask(srcType):
    skip: bool = False
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
    def validate_args(args) -> Tuple[bool, str]:
        if "dask_ignore" not in args.keys() or args["dask_ignore"] is False :
            if "dask_i" not in args.keys() or args["dask_i"] is None :
                return (False, "error: either dask_ignore or dask_i must be provided.")

        return (True,"")
    
    @staticmethod
    def should_run(args) -> bool:
        return not args["dask_ignore"]
    
    data_dir: Path
    sched_path: Path
    workr_path: Path
    wxfer_path: Path

    sched_filename: str = "SCHEDULER_df.csv"
    workr_filename: str = "WORKER_df.csv"
    wxfer_filename: str = "WORKER_TRANSFER_df.csv"

    def __init__(self, args):
        self.verbose: bool = args['verbose']
        self.data_dir = Path(args["dask_i"])

        self.sched_path = self.data_dir / self.sched_filename
        self.workr_path = self.data_dir / self.workr_filename
        self.wxfer_path = self.data_dir / self.wxfer_filename

        self.validate_files()


    def validate_files(self):
        if not self.data_dir.exists():
            raise ValueError("Provided DASK metadata directory does not exist: %s" % self.data_dir)
        
        if not self.data_dir.is_dir():
            raise ValueError("Provided DASK metadata directory path is not a directory. Please point to the directory containing all 3 output files. Provided path: %s" % self.data_dir)
        
        if not self.sched_path.exists():
            raise ValueError("Provided directory does not contain a \"%s\" file: %s" % (self.sched_filename, self.data_dir))

        if not self.workr_path.exists():
            raise ValueError("Provided directory does not contain a \"%s\" file: %s" % (self.workr_filename, self.data_dir))

        if not self.wxfer_path.exists():
            raise ValueError("Provided directory does not contain a \"%s\" file: %s" % (self.wxfer_filename, self.data_dir))

        if self.verbose: print("Found all files needed from DASK.")
