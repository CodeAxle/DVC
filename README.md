```
mkdir DVC
```

```
cd DVC
```

```
code .
```

```
conda create -p venv python==3.11 -y
```

```
conda activate venv/
```

```
git init
```

```
mkdir .gitignore
```

```
mkdir requirements.txt
```

```
pip install -r requirements.txt
```

```
dvc init
```

```
dvc repro
```

```
dvc dag
```