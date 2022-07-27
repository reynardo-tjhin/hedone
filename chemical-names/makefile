CC=gcc
FLAGS=-Wall -Werror -Wvla -fsanitize=address,leak
TARGET=main

build:
	$(CC) $(FLAGS) $(TARGET).c -o $(TARGET)
	./$(TARGET)
	rm -f $(TARGET)
