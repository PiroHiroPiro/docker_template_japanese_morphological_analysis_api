# Japanese morphological analysis API server on docker

This is a simple Japanese morphological analysis API server on Docker.

## Requirement

- [docker](https://www.docker.com/)
  - docker-compose

## Usage

Run API server:

```console
$ docker-compose up
```

`GET /parse` with `q` param
```console
$ curl -s -S --get --data-urlencode 'q=きゃりーぱみゅぱみゅ' http://localhost:8080/parse | jq .
{
  "result": [
    {
      "features": [
        "名詞",
        "固有名詞",
        "人名",
        "一般",
        "*",
        "*",
        "きゃりーぱみゅぱみゅ",
        "キャリーパミュパミュ",
        "キャリーパミュパミュ"
      ],
      "surface": "きゃりーぱみゅぱみゅ"
    }
  ]
}
```

## Install

Clone repository:

```console
$ git clone https://github.com/PiroHiroPiro/docker_template_morphological_analysis_api.git
$ cd docker_template_morphological_analysis_api
```

Build image:

```console
$ docker-compose build
```

## Licence

This software is released under the MIT License, see [LICENSE](https://github.com/PiroHiroPiro/docker_template_morphological_analysis_api/blob/master/LICENSE).

## Author

[Hiroyuki Nishizawa](https://github.com/PiroHiroPiro)
