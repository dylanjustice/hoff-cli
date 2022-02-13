import subprocess

from modules.echo import error, info, success

cmd = ["dotnet", "restore"]

class DotnetRestore:
    def run(path=""):
        """Restore the dotnet solution from the root of the project via dotnet restore """
        if path:
            cmd.append(path)
        info("Restoring nuget packages (via %s" % " ".join(cmd))


        result = subprocess.run(cmd)
        status = result.returncode

        if status != 0:
            error("Solution failed to restore. See output for details.")
            return status

        success("Dotnet solution restored!")
        return status


