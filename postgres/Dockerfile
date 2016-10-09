FROM postgres:latest

#otherwise the volumed data somehow left behind ?
ENV PGDATA /var/lib/postgresql/testnet_data

RUN mkdir -p $PGDATA

#we do want all the initialization but don't want to stuck attached to the running instance of postgres
RUN sed -i 's/exec gosu postgres "$@"/# exec gosu postgres "$@"/' /docker-entrypoint.sh
#bug in the parent image. or a nasty feature.
RUN sed -i 's/exec "$@"/# exec "$@"/' /docker-entrypoint.sh

RUN /docker-entrypoint.sh postgres
#initialiation isn't needed anymore, replace with a dummy wrapper
ADD new_entry_point.sh /docker-entrypoint.sh

ADD baseline.sh /baseline/baseline.sh
WORKDIR /baseline

RUN /baseline/baseline.sh && rm -Rf /baseline