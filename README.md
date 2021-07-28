Brandnew-flask is a CLI tool used to generate a powerful and mordern flask-app that supports the production environment.

Brandnew-flask is still in the initial stage and needs to be updated and improved continuously. Everyone is welcome to maintain and improve this CLI. 

# Table of Contents

- [Installing](#installing)
- [Usage](#usage)

## Installing

Provide several ways to install `brandnew-flask` binary toolkits.

### Install with gomod

```shell
$ export GOPATH = "YOURGOPATH"     # Check by "go env | grep GOPATH"
$ go install github.com/ysyisyourbrother/brandnew-flask@latest && sudo mv $GOPATH/bin/brandnew-flask $GOPATH/bin/brand
```

### Install with release binary

Download the latest release binary `brand` on Github.

```shell
$ sudo chmod +x brand
```

## Usage

Create framework with  `brand new`  command:

```shell
$ brand new
? Your flask-app name: myapp    (Enter)
? Your name: brandon            (Enter)
```

The framework code of flask-app will be generated in the directory where the binary file is executed. The name of the folder is the flask-app name you entered
