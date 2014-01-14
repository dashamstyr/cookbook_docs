from pybtex.database.input import bibtex
parser = bibtex.Parser()
bib_data = parser.parse_file('feedbacks.bib')
class hold(object):
    pass
the_list=[]

for the_key in bib_data.entries.keys():
    value=hold()
    value.key=the_key
    value.title=bib_data.entries[the_key].fields['title']
    value.resource=bib_data.entries[the_key].fields['resource']
    the_list.append(value)

def sort_by_key(the_value):
    return the_value.key

the_list.sort(key=sort_by_key)

# Finally, process the template to produce our final text.

# Load the jinja library's namespace into the current module.
import jinja2, os

## # In this case, we will load templates off the filesystem.
## # This means we must construct a FileSystemLoader object.
## # 
## # The search path can be used to make finding templates by
## #   relative paths much easier.  In this case, we are using
## #   absolute paths and thus set it to the filesystem root.
## thedir=os.getcwd()
## templateLoader = jinja2.FileSystemLoader( searchpath=thedir)

## # An environment provides the data necessary to read and
## #   parse our templates.  We pass in the loader object here.
## templateEnv = jinja2.Environment( loader=templateLoader )

## # This constant string specifies the template file we will use.
## TEMPLATE_FILE = "template.jinja"

## # Read the template file using the environment object.
## # This also constructs our Template object.
## template = templateEnv.get_template( TEMPLATE_FILE )

# Specify any input variables to the template as a dictionary.
template_string="""
Recent papers
_____________

{% for item in seq %}
* :cite:`{{item.key}}`:  `{{item.key}}: {{item.title}} <{{item.resource}}>`_
{%- endfor %}

.. rubric:: References

.. bibliography:: out.bib
   :style: unsrt
"""

template=jinja2.Template(template_string)

templateVars = {"seq":the_list}

# Finally, process the template to produce our final text.
outputText = template.render( templateVars )

with open('index_out.rst','w') as fh:
    fh.write(outputText)
    
