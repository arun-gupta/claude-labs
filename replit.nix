{ pkgs }: {
  deps = [
    pkgs.python39
    pkgs.python39Packages.pip
    pkgs.python39Packages.setuptools
    pkgs.python39Packages.wheel
  ];
} 