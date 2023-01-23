import argparse
import subprocess

from DatabaseServer.src.submodules.dev_tools_utils.data_configuration import LocalData


# Instantiate the parser
parser = argparse.ArgumentParser(description="DevTools description")
parser.add_argument("--start", action="store_true",
                    help="Start server in the background.")
parser.add_argument("--stop", action="store_true",
                    help="Stop server in the background.")

# Parse args
args = parser.parse_args()


def start_app():
    print("start_app()")
    raw_cmds = f"""
    cd DatabaseServer && python3.10 manage.py runserver 37002;
    """

    parsed_cmds = bytes(raw_cmds, 'utf8')
    print("Parsed cmds: ", parsed_cmds)

    # For subprocess.Popen()
    # It's recommended to use fully qualified paths, or
    # some things might be overriden
    process: subprocess.Popen = subprocess.Popen(["/bin/bash"],
                                                 stdin=subprocess.PIPE,
                                                 stdout=subprocess.PIPE,
                                                 shell=True)
    print("Process started")
    print("Its PID: ", process.pid)
    print("Pid type: ", type(process.pid))
    LocalData.save_data(
        {
            "subprocesses": {
                "pids": [process.pid]
            }
        },
        True)

    out, err = process.communicate(parsed_cmds)
    print("Communicated with subprocess")
    print(out.decode("utf-8"))


def stop_app():
    print("\nstop_app():")


# Start or stop the app
if args.start:
    start_app()

if args.stop:
    stop_app()
