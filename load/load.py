import gzip
import shutil
import os
import tempfile
import duckdb

zippedDirectory = "data/gharchive_sample/"

def unzip_json_file(srt_gz_dir, dest_json_dir, zip_file):
    """Function that unzips all gzip files in the srt_gz_dir and stores the unzipped files to dest_json_dir."""
    with gzip.open(srt_gz_dir + zip_file, "rb") as f_in:
        with open(os.path.join(dest_json_dir + "/" +zip_file[:-3]), "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)

# Provide the location of my directory to create a temp directory.
current_directory = "C:\\Users\\danie\\Documents\\Build Fellows Workspace\\github-stars-pipeline\\data"

# Create a temp directory to hold unzipped data.  
temp_dir =tempfile.mkdtemp(dir = current_directory, prefix="unzipped_data_")

# Loop through each zipped file and unzip.
for filename in os.listdir(zippedDirectory):

    # .DS_Store is macOS hidden system files that needs to be skipped when unzipping. 
    if filename == '.DS_Store':
        continue
    unzip_json_file(zippedDirectory, temp_dir, filename)


# Create a persistent DuckDB connection to my repo.
connection = duckdb.connect("github_stars.db")

# Create a 'source' schema in my 
connection.execute("CREATE SCHEMA source")


# Use SQL to create or replace the table source.src_gharchive with all the jsons. 
data = os.path.join(temp_dir + "*.json")
connection.sql(f"create or replace table source.gharchive as select * from read_json_auto('{data}')")

connection.close()


# Deleting the temp directory.
shutil.rmtree(temp_dir)

