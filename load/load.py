import gzip
import shutil
import os
import duckdb

# Setting variables for the destination folder names.
zippedDirectory = "data/gharchive_sample/"
unzippedDirectory = "data/unzipped_data/"

def unzip_json_file (srt_gz_dir, dest_json_dir):
    """Function that unzips all gzip files in the srt_gz_dir and stores the unzipped files to dest_json_dir."""
    for filename in os.listdir(srt_gz_dir):
        
        # .DS_Store is macOS hidden system files that needs to be skipped when unzipping. 
        if filename == '.DS_Store':
            continue
        
        with gzip.open(srt_gz_dir + filename, "rb") as f_in:
            with open(os.path.join(dest_json_dir + filename[:-3]), "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)


# Creating a persistent DuckDB connection to my repo.
connection = duckdb.connect("github_stars.db")

# # Create a 'source' schema in my 
# connection.execute("CREATE SCHEMA source")


# # Use SQL to create or replace the table source.src_gharchive with all the jsons. 
data = os.path.join(unzippedDirectory + "*.json")
connection.sql(f"create or replace table source.gharchive as select * from read_json_auto('{data}')")

connection.close()

# unzip_json_file(zippedDirectory, unzippedDirectory)

