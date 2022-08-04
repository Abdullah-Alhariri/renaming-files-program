<p align=center>
  <h2 align="center"> renaming-files-program </h2>
</p>

<p align="center">
 <a  align="center" target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.10.5-green.svg"></a>
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#contributing">Contributing</a>
</p>

## Installation

```console
# clone the repo
 git clone https://github.com/Abdullah-Alhariri/renaming-files-program.git

# change the working directory to renaming-files-program
 cd renaming-files-program

# install the requirements
 python -m pip install -r requirements.txt
```

## Usage

In the "options.json" you can find options. Here you can assign the key for whatever you want to replace it with (value)

```console
{
  " ": "_",
  "(": "_",
  ")": "_"
}
```

This is how you would type a command. old_folder_files is where all the files stored that you want to rename. The program will automatically copy those files and store them in a new folder("new_folder"), then it will start with renaming the files inside the new_folder

```console
python rename.py old_folder_files new_folder
    Usage: python rename.py <from folder> <new folder>
```

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request.
Don't forget to give the project a star! Thanks!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/renaming-files-program`)
3. Commit your Changes (`git commit -m 'Add some <feature>'`)
4. Push to the Branch (`git push origin feature/renaming-files-program`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>
