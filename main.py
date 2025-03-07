#!/usr/bin/env python
# coding: utf-8

from src.main_cli import base

def main():
    try:
        base()
    except KeyboardInterrupt:
        print("\nProgram terminated forcefully.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()