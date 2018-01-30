INCDIR = -I.
DBG    = -g
OPT    = -O3
CPP    = g++
CFLAGS = $(DBG) $(OPT) $(INCDIR)
LINK   = -lm

.cpp.o:
	$(CPP) $(CFLAGS) -c $< -o $@

all: segment segment_py

segment: segment.cpp segment-image.h segment-graph.h disjoint-set.h
	$(CPP) $(CFLAGS) -o segment segment.cpp $(LINK)

segment_py: segment_py.cpp segment-image.h segment-graph.h disjoint-set.h
	$(CPP) $(CFLAGS) -fPIC -shared -o segment_py.so segment_py.cpp $(LINK)

clean:
	/bin/rm -f segment *.o *.so

clean-all: clean
	/bin/rm -f *~
