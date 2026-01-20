For those working on draft workbooks, run the following actions occasionally:
- [ ] Run `python3 url_check.py 100` to check and get titles of each reference/video. Use a number like 100 to ignore checked urls in past 100 days.
- [ ] Run `python3 gather_resources.py`. Outputs in `Build/Resources-en_US`
- [ ] Run `python3 make_chapter_pdfs.py en_US`. Takes a while.
- [ ] Run `python3 build_chapterlist.py`. Outputs in `Resources-en_US/chaplist.txt` Copy this into the `github.io repository`
- [ ] Copy the output in `Build/Resources-en_US` and replace everything in [kontinuafoundation.github.io](https://github.com/KontinuaFoundation/kontinuafoundation.github.io). 

For concatenating book chapters into book_00:
```cd ../Chapters && cat book_{01..36}.txt > book_00.txt && cd ../Build```

All of these steps have been automated in `Build/deploy_to_kontinua.py`
