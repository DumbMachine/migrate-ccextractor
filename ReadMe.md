# Convert Doku
This is a small tool to convert pages from `DokuWiki` to `FastPages`.

### Requirements:

- `php`, used by a script to convert pages.

- `python`, used to correct the mistakes of above tool.

- `python packages`, run the following:

  ```bash
  $ cd convert_doku
  $ pip install -r requirements.txt
  ```

### Running:

To ways to run the script:

- using a `url` of the `DokuWiki` page:

  ```bash
  $ cd convert_doku
  $ python convert_doku_page.py --url <url_name>
  ```

- using `filename` of the `DokuWiki` page, if you have the `source` of the page in `.txt` file:

  ```bash
  $ cd convert_doku
  $ python convert_doku_page.py --file <file_name>
  ```

### Features:

Currently the tool can take care of the following:

- Renaming the page to the format required by `fastpages`, i.e, `<last_update_data>-post_name`.
- Handling the embedding of `youtube` pages.
- Handling `media`, like images. This works by linking to the media on from `https://ccextractor.org/_media/{media}`.
- Correct the mistakes of the `php` converter tool used. Big thanks to [DokuWiki-to-Markdown-Converter](https://github.com/ludoza/DokuWiki-to-Markdown-Converter). (Correct the absolute urls and relative urls by converting them to format required by `fastpages`).

### TODO:

- [ ] Some pages give exception because finding their last edit date is not allowed, eg private pages. 