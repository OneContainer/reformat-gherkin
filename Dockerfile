FROM python:3-slim AS builder

COPY . /root/

WORKDIR /root/

RUN pip install poetry && \
    poetry build && \
    pip install --user dist/reformat_gherkin*.whl

FROM python:3-slim

COPY --from=builder /root/.local/bin/reformat-gherkin /usr/bin/reformat-gherkin

ENTRYPOINT ['reformat-gherkin']
