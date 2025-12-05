# VideoDownloader

Personal project based on yt-dlp library.

## Prerequests

Make sure to add /Desktop/Kosarka/Prenosi/ !!!
Make sure to install ffmpeg !!!

## Installing FFmpeg (Windows)

### Step 1: Download

1. Open the official FFmpeg website.
2. Under **Windows** builds, follow the link to the **gyan.dev** builds.
3. On gyan.dev, download the archive:

   - For most users, `ffmpeg-release-essentials.7z` is sufficient.

### Step 2: Extract the archive

1. Extract the `.7z` file using a tool like **7-Zip**.
2. You will get a folder similar to:

   - `ffmpeg-2025-xx-xx-essentials_build`

### Step 3: Place FFmpeg next to your Python script

Create an `ffmpeg` folder in the same directory as your Python script and move the extracted build there so that the structure looks like this:

```text
VideoDownloader\
  VideoDownloader.py
  ffmpeg\
    bin\
      ffmpeg.exe
```

## Installation

Program requires [Python](https://www.python.org/downloads/) v3.9+ to run and package manager for Python (pip) instalation
```sh
py -m ensurepip --default-pip
```

[Create virtual environment](https://docs.python.org/3/library/venv.html) for this solution (you can skip this if you want to install depandencies globaly).

Go to instalation directory and run to create virtual environment:
```sh
py -m venv .venv
```

Go to virtual environment
```sh
cd .venv/Scripts
.\activate
```

Install the dependencies from requirements.txt (make sure that you are in main dir)

```sh
pip install -r requirements.txt
```

## Run app

Run batch file (make sure that virtual environment name is .venv)

## Additional

Check: https://github.com/jely2002/youtube-dl-gui