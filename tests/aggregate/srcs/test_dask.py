import pytest
from aggregate.srcs.dask import dask

def test_find_file_no_subdir(tmp_path) :
    d = tmp_path / "find_file_test"
    d.mkdir()
    f = d / "compiled_tasks.txt"
    f.write_text("test file")

    a: dask = dask(d)
    print(a.files)

def test_find_file_subdirs(tmp_path) :
    # making sure that the pathlib grob function doesn't include subfolders in its search
    d = tmp_path / "find_file_test_subdirs"
    d.mkdir()
    d2 = d / "sub"
    d2.mkdir()
    f = d / "compiled_tasks.txt"
    f.write_text("test file")
    f2 = d2 / "compiled_tasks.txt"
    f2.write_text("test file")

    a: dask = dask(d)
    print(a.files)

def test_find_file_nofile(tmp_path) :
    d = tmp_path / "find_file_test_nofile"
    d.mkdir()
    
    with pytest.raises(FileNotFoundError) as e_info :
        a: dask = dask(d)