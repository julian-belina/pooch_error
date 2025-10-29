import pooch
from pooch import Unzip

import pathlib


root_dir = pathlib.Path(__file__).parent
root_directory = root_dir.parent
data_directory = root_directory.joinpath("geokit", "data")
bathymetry_data_handler = pooch.create(
    path=data_directory, base_url="doi:10.5281/zenodo.17047388", registry=None, version_dev=None, retry_if_failed=5
)

# Automatically populate the registry so there is no need
# to register the files and hashes manually.
bathymetry_data_handler.load_registry_from_doi()

bathymetry_rasters_dir = str(data_directory.joinpath("gebco_tiles"))
# Fetch one of the files in the repository
unpack_zones_archive = Unzip(extract_dir=bathymetry_rasters_dir)
# Download and cache the offshore gebco dataset
bathymetry_data_handler.fetch("gebco_tiles.zip", processor=unpack_zones_archive)