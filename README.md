# junk-detector

Simple Python script to analyze a folder and detect encrypted blobs in it.

## How to

Just copy the `junk-detector.py` into a folder you want to analyze and run `python junk-detector.py`. By default, it will analyze every file in every subdirectory. It currently supports two alphabets: English alphabet and the Russian alphabet. If you need to analyze some other alphabet, feel free to [report an issue](https://github.com/aleksandar-todorovic/junk-detector.py/issues/new).

## Options

You can tweak the script to do the following:

* Exclude the first line (often used for the headers of a file)
* Add additional dictionaries if you expect the non-encrypted files to be written in some other language.
* Change the location of the output file (by default, the output gets stored in `/tmp/output.csv`)
* Change the location of a directory you want to analyze (it doesn't have to be the one your file is in)
* Specify file extension that you want to analyze.

If you want to do some of these things, just open up the script in your favorite text editor and pay attention to the comments.

## Output

By default, the output is written in `/tmp/output.csv`. That `.csv` file contains four columns:

1. Name and location of the file
2. Percentage of Russian characters in a file
3. Percentage of English characters in a file
4. Percentage of other Unicode characters

Note that, by default, the script completely ignores the following characters: `1234567890 ,.-`.

## License

This script is licensed under the [MIT license](https://github.com/aleksandar-todorovic/junk-detector.py/blob/master/LICENSE).
