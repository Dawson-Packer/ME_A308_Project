CC = avr-gcc
CFLAGS = -Wall -std=c++11 -DUBRRH

# Include paths for libraries and Arduino core
INCLUDE_PATH = \
    -IC:\\Users\\Dawson\\AppData\\Local\\arduino15\\packages\\arduino\\hardware\\avr\\1.8.6\\cores\\arduino \
    -IC:\\Users\\Dawson\\AppData\\Local\\arduino15\\libraries\\Ethernet\\src \
    -IC:\\Users\\Dawson\\AppData\\Local\\arduino15\\libraries\\Firmata \
    -IC:\\Users\\Dawson\\AppData\\Local\\arduino15\\libraries\\Keyboard\\src \
    -IC:\\Users\\Dawson\\AppData\\Local\\arduino15\\libraries\\LiquidCrystal\\src \
    -IC:\\Users\\Dawson\\AppData\\Local\\arduino15\\libraries\\Mouse\\src \
    -IC:\\Users\\Dawson\\AppData\\Local\\arduino15\\libraries\\SD\\src \
    -IC:\\Users\\Dawson\\AppData\\Local\\arduino15\\libraries\\Servo\\src \
    -IC:\\Users\\Dawson\\AppData\\Local\\arduino15\\libraries\\Stepper\\src \
    -IC:\\Users\\Dawson\\AppData\\Local\\arduino15\\libraries\\TFT\\src \
    -IC:\\Users\\Dawson\\AppData\\Local\\arduino15\\packages\\arduino\\hardware\\avr\\1.8.6\\libraries\\EEPROM\\src \
    -IC:\\Users\\Dawson\\AppData\\Local\\arduino15\\packages\\arduino\\hardware\\avr\\1.8.6\\libraries\\HID\\src \
    -IC:\\Users\\Dawson\\AppData\\Local\\arduino15\\packages\\arduino\\hardware\\avr\\1.8.6\\libraries\\SoftwareSerial\\src \
    -IC:\\Users\\Dawson\\AppData\\Local\\arduino15\\packages\\arduino\\hardware\\avr\\1.8.6\\libraries\\SPI\\src \
    -IC:\\Users\\Dawson\\AppData\\Local\\arduino15\\packages\\arduino\\hardware\\avr\\1.8.6\\libraries\\Wire\\src \
    -IC:\\Users\\Dawson\\AppData\\Local\\arduino15\\packages\\arduino\\hardware\\avr\\1.8.6\\variants\\standard \
    -ID:\\Developer\\tools\\avr8-gnu-toolchain-win32_x86_64\\avr\\include \
    -Iinclude

# Arduino source file
SRC = main/main.ino

# Output file (your compiled object)
OBJ = main.o

# The final output program
OUT = main.elf

# Default target
all: $(OUT)

$(OUT): $(OBJ)
	$(CC) $(OBJ) -o $(OUT)

$(OBJ): $(SRC)
	$(CC) $(CFLAGS) $(INCLUDE_PATH) -c $(SRC) -o $(OBJ)

clean:
	rm -f $(OBJ) $(OUT)

.PHONY: all clean