# Jupyter Notebook

I am running JupyterNotebook from a container: 
```
docker run -p 8888:8888 jupyter/scipy-notebook

I 2022-01-01 04:00:49.117 LabApp] JupyterLab extension loaded from /opt/conda/lib/python3.9/site-packages/jupyterlab
[I 2022-01-01 04:00:49.117 LabApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
[I 04:00:49.122 NotebookApp] Serving notebooks from local directory: /home/jovyan
[I 04:00:49.122 NotebookApp] Jupyter Notebook 6.4.6 is running at:
[I 04:00:49.122 NotebookApp] http://b0d8253f349b:8888/?token=a8cd9b1ae5b339454d2045e3cec04bbffaf71c84fcec40ec
[I 04:00:49.123 NotebookApp]  or http://127.0.0.1:8888/?token=a8cd9b1ae5b339454d2045e3cec04bbffaf71c84fcec40ec
[I 04:00:49.123 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 04:00:49.127 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/nbserver-7-open.html
    Or copy and paste one of these URLs:
        http://b0d8253f349b:8888/?token=a8cd9b1ae5b339454d2045e3cec04bbffaf71c84fcec40ec
     or http://127.0.0.1:8888/?token=a8cd9b1ae5b339454d2045e3cec04bbffaf71c84fcec40ec

```

# Links
- https://github.com/jupyter/docker-stacks
- https://jupyter-docker-stacks.readthedocs.io/en/latest/
