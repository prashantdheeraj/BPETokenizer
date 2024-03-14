# 1. Source Article 
## For building Library: https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f
## For building Tokenizer: https://github.com/karpathy/minbpe 


# 2. Create Virtual Environment
## Create Virtual environment : ` % python3 -m venv venv `
## Activate Virtual environment : `% source venv/bin/activate`

# Install libraries for library creation
`% pip install wheel`
`% pip install setuptools`
`% pip install twine`

# 3. Create Folder Structure
## under root folder create the following
### setup.py
### README.md
### Folder with the Library name (BPE Tokenizer): Inside this folder create
#### __init__.py : Any folder that has an __init__.py file in it, will be included in the library when we build it. Most of the time, you can leave the __init__.py files empty. Upon import, the code within __init__.py gets executed, so it should contain only the minimal amount of code that is needed to be able to run your project. 
#### file(s) with the functionality
### Test Folder. Inside thetest folder create
#### __init__.py
#### test file(s)

# 4. Write the content inside the libraray folder (BPEToeknizer)
## write miniaml code in __init__.py
## write base.py
## write basic.py inheriting base.py
## write regex.py inhereting base.py
## For testing do the following
### `pip install pytest`
### `pip install pytest-runner`
### write content of test_tokenizer.py

# 5. Build the library