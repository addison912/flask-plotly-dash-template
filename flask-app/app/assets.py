"""Compile static assets."""
def compile_static_assets(assets):
    """
    Compile stylesheets if in development mode.

    :param assets: Flask-Assets Environment
    :type assets: Environment
    """
    assets.auto_build = True
    assets.debug = False
    return assets
