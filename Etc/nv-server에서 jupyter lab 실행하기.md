# jupyter lab 실행하기



how to open jupyter9090 

port is already registered. so use new port example 9998 assume you will use 9998



<br/>

### START



cmd 열기



connect

````
sft ssh raplab-hackathon
````



allocate GPU node

```
srun --pty --gpus 1 bash
```



check your compute node name dgx01xx

ex) dgx0180



singularity run which include lab

```
singularity run --nv ***.simg jupyter lab --ip=0.0.0.0 --port=9998 --no-browser --NotebookApp.token=''
```



open another console and connect with port forwarding

```
sft -L 9998:dgx01xx:9998 raplab-hackathon
```

ex) dgx0180



connect browser [http://localhost:9998](http://localhost:9998/)



if console is idle, connection is closed. you turn on top option on second console







jupyter notebook를 열고 싶은 경우 jyputer lab 를 jupyter notebook로 변경해주면 된다. 