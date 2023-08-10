# Development Settings

import subprocess



def start_uvicorn():
    try:
        subprocess.run(["uvicorn", "settings.start:app", "--host", "0.0.0.0", "--port", "8000", "--reload"])
    except KeyboardInterrupt:
        print("\nUvicorn server was terminated.")



def main():

    start_uvicorn()
    




if __name__ == "__main__":
    main()

