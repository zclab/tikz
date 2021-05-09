import os
import subprocess
from pathlib import Path


class BuildLatex:

    def __init__(
        self,
        *,
        main_file: str,
        builder: str = "xelatex"
    ) -> None:
        """Command for building latex output.

        Parameters
        ----------
        main_file : str
            The main file of latex project.
        builder : str, optional
            command used for building the output, by default "xelatex"
        """
        self._builder = builder
        self._main_file = Path(main_file)

    @property
    def builder(self) -> str:
        """command used for building the output

        Returns
        -------
        str
            command used for building the output
        """
        return self._builder

    @property
    def main_file(self) -> Path:
        """The main file of latex project.

        Returns
        -------
        Path
            The main file of latex project.
        """
        return self._main_file

    def _run(
        self,
        ref: bool = False
    ) -> None:
        """Building command.

        Parameters
        ----------
        ref : bool, optional
            Used for correctly output reference of the latex project, by default False
        """
        c = "cd {} && ".format(self.main_file.parent)
        if ref:
            c += 'bibtex ' + self.main_file.with_suffix('.aux').name
        else:
            c += self.builder + ' ' + self.main_file.name
        subprocess.run(c, shell=True)

    def _open(self) -> None:
        """Open output file after building.
        """
        c = "cd {} && open ".format(self.main_file.parent)
        c += self.main_file.with_suffix('.pdf').name
        subprocess.run(c, shell=True)

    def build(
        self,
        *,
        clean_suffix: bool = True,
        open_file: bool = True
    ) -> None:
        """Build the output of the latex project.

        Parameters
        ----------
        clean_suffix : bool, optional
            Clean the unused files or not, by default True
        open_file : bool, optional
            Open output file after building or not, by default True
        """

        self._run()
        if self.main_file.with_suffix('.aux').exists():
            self._run(ref=True)
            self._run()
            self._run()
        if clean_suffix:
            BuildLatex.clean()
        if open_file:
            self._open()

    @staticmethod
    def clean(*suffix, exclude_dirs=None):
        """Clean the unused files

        Parameters
        ----------
        exclude_dirs : [type], optional
            Directory that should not considered when cleaning unused files, by default None
        """
        if not suffix:
            suffix = (".bbl", ".blg", ".out", ".aux", ".log", ".toc")

        excluded = {".git", ".vscode", ".idea"}
        if exclude_dirs:
            excluded.union(exclude_dirs)

        for root, dirs, files in os.walk("."):
            if not any([d in root for d in excluded]):
                for f in files:
                    file = Path(root) / f
                    if file.suffix in suffix:
                        subprocess.run("rm {}".format(file), shell=True)
