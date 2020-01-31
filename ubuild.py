from uranium import current_build

current_build.packages.install("uranium-plus[vscode]")
import uranium_plus

current_build.config.update(
    {
        "uranium-plus": {
            "module": "pelican-to-wordpress",
            "test": {"packages": []},
        }
    }
)

uranium_plus.bootstrap(current_build)
