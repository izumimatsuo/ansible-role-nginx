#!/bin/sh

docker build . -t ansible/test-runner
docker run --name runner -v /var/run/docker.sock:/var/run/docker.sock -v `pwd`:/root/build -td ansible/test-runner
docker exec -it runner bash -c "cd /root/build/tests && ansible-playbook test.yml --syntax-check"
docker exec -it runner bash -c "cd /root/build/tests && ansible-playbook test.yml && py.test -v test.py --hosts="docker://localhost""
docker rm -f runner localhost
