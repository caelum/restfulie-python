LOCAL_MAKEFILE=$(wildcard ../Makefile*)
include $(LOCAL_MAKEFILE)

all: restfulie_client

restfulie_client:
	cd client && make

