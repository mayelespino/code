# Jupyter Notebook

I am running JupyterNotebook from a container: 
```
docker run -p 8888:8888 jupyter/scipy-notebook


    To access the notebook, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/nbserver-7-open.html
    Or copy and paste one of these URLs:
        http://b0d8253f349b:8888/?token=a8cd9b1ae5b339454d2045e3cec04bbffaf71c84fcec40ec
     or http://127.0.0.1:8888/?token=a8cd9b1ae5b339454d2045e3cec04bbffaf71c84fcec40ec

```
make sure to copy the token, it will generate a new one each time, use it to login. Setting up the password does not take.

To run while mounting a local path on to the container, so that I can save the notebooks there, use this:

```
docker run -p 8888:8888 -v /path/to/Notebooks:/home/ jupyter/scipy-notebook
```

# Links
- https://github.com/jupyter/docker-stacks
- https://jupyter-docker-stacks.readthedocs.io/en/latest/
