from typing import Tuple
from . import srcs
from . import snks

import argparse as ap

def get_known_sources() :
    sources = dict([(name, cls) for name, cls in srcs.__dict__.items() if isinstance(cls, type) and not cls.skip])
    return sources

def get_known_sinks() :
    sinks = dict([(name, cls) for name, cls in snks.__dict__.items() if isinstance(cls, type)])
    return sinks

def main():
    # print("Hello from wfmeta-aggregate!")
    # print(get_known_sources())
    # print(get_known_sinks())

    so: dict[str, type] = get_known_sources()
    sk: dict[str, type] = get_known_sinks()

    parser: ap.ArgumentParser = create_argparse(so,sk)
    args = vars(parser.parse_args())
    (all_found, err) = check_requirements(args, so)
    if not all_found :
        print(err)
        parser.print_usage()
        exit(1)

    if args['verbose']: print("All parameter requirements fulfilled. Initializing sources.")

    initialized_sources: dict[str, srcs.srcType] = {}
    for (source_name, source_type) in so.items():
        if source_type.should_run(args):
            initialized_sources[source_name] = source_type(args)
    
# TODO: make tests
def create_argparse(sources: dict[str, type], sinks: dict[str, type]) :
    parser = ap.ArgumentParser(
        prog="wfmeta-agg",
        description="Collects metadata extracted by other RECUP wfmeta tools and collects them into a singular package."
    ) 
    parser.add_argument("--verbose", action="store_true")

    # for every source, need an "input" parameter
    for (sname, sclass) in sources.items() :
        sclass.make_args(parser)

    output_opts = list(sinks.keys())
    parser.add_argument("--out-format", choices=output_opts,
                        help="Output format to collect metadata into.")
    parser.add_argument("--out-loc", 
                        help="Output location.")
    
    return parser

def check_requirements(args, sources: dict[str, type]) -> Tuple[bool, str]:
    res: bool = True
    err: str = ""
    for (_, sclass) in sources.items():
        (res_r, err_r) = sclass.validate_args(args)
        if not res_r:
            res = False
            err = err + "\n" + err_r

    err = err.strip()
    return (res,err)
