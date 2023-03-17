"""
This is a working sample CloudBolt plug-in for you to start with. The run method is required,
but you can change all the code within it. See the "CloudBolt Plug-ins" section of the docs for
more info and the CloudBolt forge for more examples:
https://github.com/CloudBoltSoftware/cloudbolt-forge/tree/master/actions/cloudbolt_plugins
"""
from common.methods import set_progress


def run(job, *args, **kwargs):
  input = "{{ noop_input }}"
  input_2 = {{ input_with_opts }}
  
  print("Input", input)
  print("Input 2", input_2)
  print("Kwargs", kwargs)
  
  return "SUCCESS", input, ""


def generate_options_for_input_with_opts(field, **kwargs):
    """
    A working sample that returns a dynamically generated list of options.

    :param field: The field you are generating options for (of type CustomField or its subclass HookInput).

    See the "Generated Parameter Options" section of the docs for more info and the CloudBolt forge
    for more examples: https://github.com/CloudBoltSoftware/cloudbolt-forge/tree/master/actions/cloudbolt_plugins
    """

    # Otherwise, define the database values and labels as a list of 2-tuples.
    options = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
    ]

    return {
        'options': options,
    }