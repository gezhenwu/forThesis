CC = g++
# CFLAGS = -lpthread

TARGET  = libPebFelix.so
# TARGET  = libPebFelix
OBJ_DIR = ./obj
SRC_DIR = ./src
INCLUDE = -I$(BASEDIR)"/flxcard" -I$(BASEDIR)"/ftools/src" -I$(BASEDIR)"/regmap" -I$(BASEDIR)"/drivers_rcc"
LIBS = -L$(BASEDIR)"/x86_64-centos7-gcc11-opt/ftools" -l"FlxTools"
SRC = $(wildcard $(SRC_DIR)/*.cpp)
OBJECTS = $(patsubst $(SRC_DIR)/%.cpp, %.o, $(SRC))

VPATH = $(SRC_DIR)
vpath %.o $(OBJ_DIR)

all: $(TARGET)

$(TARGET) : $(OBJECTS)
	$(CC) -fPIC -shared -o $@ $(addprefix $(OBJ_DIR)/, $(OBJECTS)) $(LIBS)

# $(TARGET) : $(OBJECTS)
# 	$(CC) -o $@ $(addprefix $(OBJ_DIR)/, $(OBJECTS)) $(LIBS)

%.o : %.cpp
	$(CC) -fPIC $(INCLUDE) -c $< -o $(OBJ_DIR)/$@

.PHONY : clean
clean:
	rm -rf $(TARGET) $(OBJ_DIR)/*.o ./*.o
