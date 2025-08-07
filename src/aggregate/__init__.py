from . import srcs
from . import snks

import argparse as ap

def get_known_sources() :
    sources = dict([(name, cls) for name, cls in srcs.__dict__.items() if isinstance(cls, type)])
    return sources

def get_known_sinks() :
    sinks = dict([(name, cls) for name, cls in snks.__dict__.items() if isinstance(cls, type)])
    return sinks

def main():
    print("Hello from wfmeta-aggregate!")
    print(get_known_sources())
    print(get_known_sinks())

    so = get_known_sources()
    sk = get_known_sinks()
    print(so["dask"].long_name)

    parser = create_argparse(so,sk)
    args = vars(parser.parse_args())
    print(check_requirements(args, so))
    
# TODO: make tests
def create_argparse(sources: dict[str, type], sinks: dict[str, type]) :
    parser = ap.ArgumentParser(
        prog="wfmeta-agg",
        description="Collects metadata extracted by other RECUP wfmeta tools and collects them into a singular package."
    ) 

    # for every source, need an "input" parameter
    for (sname, sclass) in sources.items() :
        sclass.make_args(parser)

    output_opts = list(sinks.keys())
    parser.add_argument("--out-format", choices=output_opts,
                        help="Output format to collect metadata into.")
    parser.add_argument("--out-loc", 
                        help="Output location.")
    
    parser.print_help()
    return parser

def check_requirements(args, sources: dict[str, type]) -> bool :
    res = True
    for (_, sclass) in sources.items() :
        res = res and sclass.validate_args(args)
    return res
