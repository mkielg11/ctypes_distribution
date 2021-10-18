ifdef SystemRoot
ENVIRONMENT_DETECTED := Windows
else
SHELL := /bin/bash
UNAME := $(shell uname)
ifneq ($(filter CYGWIN%,$(UNAME)),)
ENVIRONMENT_DETECTED := Cygwin
FIXPATH = $(subst C:,/cygdrive/c,$(subst \,/,$(1)))
else
ifneq ($(filter MINGW%,$(UNAME)),)
ENVIRONMENT_DETECTED := MinGW
FIXPATH = $(1)
else
ifneq ($(filter Linux%, $(UNAME)),)
ENVIRONMENT_DETECTED := Linux
FIXPATH = $(subst C:,c,$(subst \,/,$(1)))
endif
endif
endif
endif

SRCDIR=$(call FIXPATH,$(CURDIR)), $(call FIXPATH,$(CURDIR)/include)
OUTDIR=$(call FIXPATH,$(CURDIR)/../build_winx64)

OBJS = $(OUTDIR)/cfile.o

ifeq ($(ENVIRONMENT_DETECTED),Cygwin)
CC=x86_64-w64-mingw32-gcc
else ifeq ($(ENVIRONMENT_DETECTED),Linux)
CC=x86_64-w64-mingw32-gcc
else
$(error Unsupported environment: $(ENVIRONMENT_DETECTED))
endif

$(warning $(OBJS))

vpath %.c $(SRCDIR)

CFLAGS+= -Wall $(foreach dir, $(SRCDIR), -I$(dir)) -O2

all: $(OUTDIR)/cfile.dll

# $(OBJS): | checkdirs

$(OUTDIR)/%.o: %.c
				$(CC) $(CFLAGS) -c -o $@ $<

$(OUTDIR)/cfile.dll: $(OBJS)
				$(CC) $(CFLAGS) -o $@ -shared $^

checkdirs: $(OUTDIR)

$(OUTDIR):
				mkdir $(OUTDIR) #$(subst /,\\,$@)

clean:
				rm -f $(OUTDIR)/*.o
				rm -f $(OUTDIR)/*.dll
