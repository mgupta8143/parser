# Parser

This toy application that allows a client to specify custom operators, languages, and 
custom parsers to map expressions in a generic fashion.

A simple example could be
```
(3 * 2) + 4 = 10
```

Users can provide "expressions" such as the one above, and define custom "operators" like (*) or + above, along with a "language" such as "3" and "2" and the parenthesis to determine how expressions get evaluated. For all intents and purposes, this application is not meant to support any type of worfklow; but was created as an experiment to see how far we could push a generic parser that can be specified at run-time. 

Ideally, in the computer science world, there are other representations of such systems such as grammars and regex expressions that allow the evaluation of arbitrary strings; and are much more powerful in theory. One of the cool things about this system is the potential for "side-effects" to occur which each parsing step. 

By: manu