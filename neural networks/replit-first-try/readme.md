## Console output:
Traceback (most recent call last):
  File "/home/runner/workspace/main.py", line 1, in <module>
    import gradio as gr
  File "/home/runner/workspace/.pythonlibs/lib/python3.11/site-packages/gradio/__init__.py", line 3, in <module>
    import gradio._simple_templates
  File "/home/runner/workspace/.pythonlibs/lib/python3.11/site-packages/gradio/_simple_templates/__init__.py", line 1, in <module>
    from .simpledropdown import SimpleDropdown
  File "/home/runner/workspace/.pythonlibs/lib/python3.11/site-packages/gradio/_simple_templates/simpledropdown.py", line 6, in <module>
    from gradio.components.base import Component, FormComponent
  File "/home/runner/workspace/.pythonlibs/lib/python3.11/site-packages/gradio/components/__init__.py", line 1, in <module>
    from gradio.components.annotated_image import AnnotatedImage
  File "/home/runner/workspace/.pythonlibs/lib/python3.11/site-packages/gradio/components/annotated_image.py", line 7, in <module>
    import gradio_client.utils as client_utils
  File "/home/runner/workspace/.pythonlibs/lib/python3.11/site-packages/gradio_client/__init__.py", line 1, in <module>
    from gradio_client.client import Client
  File "/home/runner/workspace/.pythonlibs/lib/python3.11/site-packages/gradio_client/client.py", line 27, in <module>
    import httpx
  File "/home/runner/workspace/.pythonlibs/lib/python3.11/site-packages/httpx/__init__.py", line 15, in <module>
    from ._main import main
  File "/home/runner/workspace/.pythonlibs/lib/python3.11/site-packages/httpx/_main.py", line 8, in <module>
    import click
  File "/home/runner/workspace/.pythonlibs/lib/python3.11/site-packages/click/__init__.py", line 8, in <module>
    from .core import Argument as Argument
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 936, in exec_module
  File "<frozen importlib._bootstrap_external>", line 1069, in get_code
  File "<frozen importlib._bootstrap_external>", line 729, in _compile_bytecode
EOFError: marshal data too short