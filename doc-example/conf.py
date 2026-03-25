project = 'Test sphinx project'
author = 'Alice, Bob'
release = '0.1'            
                                                                                
extensions = ['myst_parser', "autodoc2"]
                                                                                
exclude_patterns = ['_build']

autodoc2_packages = [
    "multiply.py"
]