import pyi_splash

pyi_splash.update_text("Loading Sample Builder...")

from orso_sample_builder.__main__ import main

# done loading modules
pyi_splash.close()

if __name__ == "__main__":
    main()
