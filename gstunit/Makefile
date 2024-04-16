# Compiler
CC := gcc

# Directories
GSTUNIT_DIR := .
GSTUNIT_INCLUDE_DIR := $(GSTUNIT_DIR)/include
GSTUNIT_SRC_DIR := $(GSTUNIT_DIR)
GSTUNIT_OBJ_DIR := $(GSTUNIT_DIR)/obj
CLI_DIR := cli
CLI_INCLUDE_DIR := $(CLI_DIR)/include
CLI_SRC_DIR := $(CLI_DIR)/src
CLI_OBJ_DIR := $(CLI_DIR)/obj

# Source files
GSTUNIT_SRC_FILES := $(wildcard $(GSTUNIT_SRC_DIR)/*.c)
CLI_SRC_FILES := $(wildcard $(CLI_SRC_DIR)/*.c)

# Object files
GSTUNIT_OBJ_FILES := $(GSTUNIT_SRC_FILES:$(GSTUNIT_SRC_DIR)/%.c=$(GSTUNIT_OBJ_DIR)/%.o)
CLI_OBJ_FILES := $(CLI_SRC_FILES:$(CLI_SRC_DIR)/%.c=$(CLI_OBJ_DIR)/%.o)

# Compiler flags
CFLAGS := -Wall -Wextra -Wpedantic -g -MMD -I$(GSTUNIT_INCLUDE_DIR) -I$(CLI_INCLUDE_DIR) -I/usr/include/python3.11

# Library name
LIB_NAME := libgstunit.a

# Executable name
EXECUTABLE := cli

# Main target
all: $(LIB_NAME) $(EXECUTABLE)

# Rule to compile object files for libgstunit
$(GSTUNIT_OBJ_DIR)/%.o: $(GSTUNIT_SRC_DIR)/%.c | $(GSTUNIT_OBJ_DIR)
	@$(CC) $(CFLAGS) -c $< -o $@

# Rule to compile object files for cli
$(CLI_OBJ_DIR)/%.o: $(CLI_SRC_DIR)/%.c | $(CLI_OBJ_DIR)
	@$(CC) $(CFLAGS) -c $< -o $@

# Rule to create the library
$(LIB_NAME): $(GSTUNIT_OBJ_FILES)
	@ar rcs $@ $^

# Rule to link the executable
$(EXECUTABLE): $(CLI_OBJ_FILES) $(LIB_NAME)
	@$(CC) $(CFLAGS) -L$(GSTUNIT_DIR) $^ -o $@

# Create obj directories if they don't exist
$(GSTUNIT_OBJ_DIR) $(CLI_OBJ_DIR):
	@mkdir -p $@

# Clean target
clean:
	@rm -rf $(GSTUNIT_OBJ_DIR) $(CLI_OBJ_DIR) $(LIB_NAME) $(EXECUTABLE)

# Include dependency files
-include $(GSTUNIT_OBJ_FILES:.o=.d)
-include $(CLI_OBJ_FILES:.o=.d)

.PHONY: all clean
