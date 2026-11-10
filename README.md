# CSL_auto_tag.py

Given a CSL formatted json file output from Zotero, auto-generate ID tags

To run example from command line:

`python CSL_auto_tag.py --cslFile testCSL.json`

it will output testCSL_autofmt.json with a new id tag.  The tag will follow this format:
    
    * lastNameOfFirstAuthor_year_kw1_kw2_replicate
    * where kw1 and kw2 are the first and second words in the title with three or more letters (excluding a subset of common words e.g. "the", "and", etc.), and replicate is a sequential alphabetic index starting at "a"

**Note:**  This should function fine in most circumstances, the only time it could cause issues is when you add have an existing csl file and corresponding document, to which you acc another paper with matching author, year, and keywords.  The replicate index value is not granted to match the existing order in that case.  It will if the added citation is appended to at the end of the csl document, but it will fail if the added citation is placed above/in front of the existing document.
