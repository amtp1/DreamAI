# DreamAI-Gen

## Install dependecies

```shell
pipenv install
```

## Run script

```shell
uvicorn main:app --host localhost --port 8000 --reload
```

## DreamAI-Gen API

### Get Styles

```http
GET /getStyles
```

### Generate Image

```http
GET /generateImage/programmer/84
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `programmer` | `string` | **Required**. Prompt |
| `84` | `int` | **Required**. Style Id |