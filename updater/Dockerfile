FROM public.ecr.aws/sam/build-python3.9:latest-arm64 AS builder
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV CARGO_ROOT /root/.cargo/
ENV PATH $CARGO_ROOT/bin:$PATH
WORKDIR /build
COPY requirements.txt  .
# Need to build deltalake because of the following error in manylinux wheel as of 0.7.0
#   "Unable to import module 'updater.handle': /var/task/deltalake/_internal.abi3.so: undefined symbol: renameat2"
ENV PIP_NO_BINARY=deltalake
RUN pip3 install -r requirements.txt --target ./venv

FROM public.ecr.aws/lambda/python:3.9-arm64
COPY . ${LAMBDA_TASK_ROOT}
COPY --from=builder /build/venv ${LAMBDA_TASK_ROOT}
CMD [ "updater.handle.handler" ]
