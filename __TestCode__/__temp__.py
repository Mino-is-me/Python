import unreal
import importlib
from Lib import __lib_topaz__ as topaz
from Lib import __lib_kafka__ as kafka

selected = topaz.get_selected_asset()

print(selected.__class__)


unreal.AssetToolsHelpers.get_asset_tools().redire