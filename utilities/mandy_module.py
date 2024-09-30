#!/usr/bin/env python

"""
=======================================================
Mandy's Homemade General Classes & Functions for Python
=======================================================
Mandy Renfro (2024)

Want to make your programming life easier? Import this module and enjoy my useful tools.
- At the top of your new .py or .ipynb, type:
    from mandy_module import [specific item(s) you want to use]
- Read the embedded documentation for proper care and feeding of these code critters.

Module Contents (updated 17 August 2024):
- DataCaddy (Class)
- lookup_code (Function)
"""
import inspect
import re
gather_re = r'(^ *)({0}.*?\n)(.*?)(?=\n\1?[^ \n\r#])'


class DataCaddy(object):
    """ Dynamic contain system for executing functions stored as attributes in the instance.
        ## Use 1: Automatically filling in the arguments for functions based on the attributes its already holding.
            - Temporarily substitute a held value with a keyword argument during a function call.
            - Unheld arguments can be specified either as keyword arguments or ordered arguments in the order of the unspecifed remaining arguments.
        ## Use 2: It's similar to sklearn Bunch()
            - Get or set attributions of any kind with container.[name] approach
        ## Use 3: Abbreviating function calls because you can name both the function and unchanging parameters.
        Inputs:
        - *args: should only be functions or methods because the class needs to know their __name__
        - **kwargs: can be anything
        Output:
        - Individual container of stored functions and/or attributes (functions/attributes can be added after initialization)
    """
    def __init__(self, *args, **kwargs):
        super(DataCaddy, self).__init__()
        ## Instance takes named variables and functions and automatically calls 
        ## functions based on the inputs it has in "self" or given at runtime
        self.attributes = dict()
        self.functions = dict()
        self.arg_req = dict()
        kwargs = kwargs.copy()
        for a in args:
            kwargs[a.__name__] = a
        for key in kwargs:
            if inspect.isfunction(kwargs[key]) or inspect.ismethod(kwargs[key]):
                self.functions[key] = self.wrapper(kwargs[key])
                self.arg_req[kwargs[key].__name__] = inspect.getfullargspec(kwargs[key])[0]
            else:
                self.attributes[key] = kwargs[key]
    def __setattr__(self, name, value):
        ## Base function called when you try to set a value with .[name]
        if hasattr(self, name) or name in ["attributes", "functions", "arg_req"]:
            object.__setattr__(self, name, value)
        else:
            if inspect.isfunction(value) or inspect.ismethod(value):
                self.functions[name] = self.wrapper(value)
                self.arg_req[value.__name__] = inspect.getfullargspec(value)[0]
            else:
                self.attributes[name] = value
    def __getattr__(self, name):
        ## Base function that gets the attribute value with [name]
        if name in ["attributes", "functions", "arg_req"]:
            return self.__getattribute__(name)
        if name in self.attributes:
            return self.attributes[name]
        if name in self.functions:
            return self.functions[name]
        return self.__getattribute__(name)
    def delete(self, **names):
        ## Function to remove held functions or attributes 
        for name in names:
            if name in self.attributes:
                del self.attributes[name]
            if name in self.functions:
                del self.functions[name]
                del self.arg_req[name]
    def wrapper(self, func):
        ## When a function is give to the class, function is "decorated" (it ate the inserted function to call later).
        ## When that function is called, it automatically substitutes held kwargs into the funtions required arguments.
        ## Inserts unnamed arguments into any still undefined keywords, in order.
        def call(*args, **kwargs): ## Nesting functions in this way allows delayed execution (scope container)
            kw = dict()
            non_defaults = []
            func_args = self.arg_req[func.__name__]
            for key in func_args:
                if key in kwargs:
                    kw[key] = kwargs[key]
                    non_defaults.append(key)
                elif key in self.attributes:
                    kw[key] = self.attributes[key]
                    non_defaults.append(key)
                ## Else, it better be a default value or it will say something wasn't defined
            if len(args) > 0: ## Or that it is in args
                i = 0
                for a in func_args: ## See what is left
                    if not a in kw:
                        kw[a] = args[i]
                        i += 1
                        if i > len(args):
                            break
            return func(**kw)
        ## Returns the inner function which has the inserted function within its scope as "func"
        return call ## Call is the not-yet executed function holding the wrapped function

if __name__ == "__main__": ## Won't initialize if mandy_module is imported
    ## Sample use of DataCaddy class
    import numpy as np
    def my_cool_function(alphas, betas, p_alpha, p_beta):
        print("Alpha Residuals", np.std(alphas - p_alpha))
        print("Beta Residuals", np.std(betas - p_beta))
        print("")
    alphas = np.arange(0.1, 1.3, 0.1)
    betas  = np.arange(0.0, 1.1, 0.1)
    container = DataCaddy(my_cool_function, alphas = alphas, betas = betas)
    container.my_cool_function(p_alpha = 0.6, p_beta = 1.1)
    container.my_cool_function(p_alpha = 0.9, p_beta = 0.2)
    print("#1", container.alphas, "\n", container.betas)
    container.my_cool_function(alphas = np.arange(1, 11, 1), p_alpha = 0.9, p_beta = 0.2)
    container2 = DataCaddy(my_cool_function, alphas = alphas, betas = np.arange(-1.3, 1.31, 0.1))
    container2.my_cool_function(0.6, -1.3)
    print("#2", container2.alphas, "\n", container2.betas)


## ================================================================================================


def lookup_code(source, optional_module_search = None): 
    """ Allows inspection of source code for imported functions, methods, or classes
    Important limitations:
        - Cannot provide source code for native python functions
        - Cannot provide source code that isn't contained within a single file
    Input:
        -  source: module containing the function you wish to inspect, wrapped by inspect.findsource()
        -  optional_module_search: used to manually search for specific targets
            - Requires defining keyword (i.e., "class" or "def")
        -- EXAMPLE: lookup_code(bernoulli.logpmf)
    Output:
        -  Raw code for target function, method, or class
            -  May or may not contain explanatory documentation provided by developers
    """
    source2 = inspect.findsource(source) ## variable containing findsource() function
    lines = "" ## create new empty string
    for line in source2[0]: ## iterates through raw code of target
        lines += line ## add each line to string
    text = source.__name__ ## get the name of the function, method, or class (hereafter "target")
    if inspect.ismodule(source): ## checks if target is an entire module
        if optional_module_search is not None: ## are you performing a manual search?
            text = optional_module_search ## if so, make sure to specify def or class keyword
        else: ## not a manual search
            print(lines)
            return
    elif inspect.isfunction(source) or inspect.ismethod(source): ## checks if target is a function or method
        text = "def " + text ## redefines text to include proper keyword
    elif inspect.isclass(source): ## if a class
        text = "class " + text ## redefines text to include "class" keyword
    ## instantiating compile gather_re with string you're looking for .formatted into it
    find_re = re.compile(gather_re.format(text), flags = re.MULTILINE|re.DOTALL)
    for m in re.finditer(find_re, lines): ## find all matches in module
        matched = m.group() ## match for the target and its content
        print(matched) ## prints target and content