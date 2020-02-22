import json

from AnalysisData import AnalysisDataModle

# -------------------------------------------------------------------------------------------------------------------- #

# 抓包数据 文件
request_json_file = '../data/request_data.json'
# 冰鸟接口 配置文件
bn_config_json_file = '../data/config/bn_config_data.json'
# 发行接口 配置文件
fx_config_json_file = '../data/config/fx_config_data.json'
# 轻度接口 配置文件
qd_config_json_file = '../data/config/qd_config_data.json'

# -------------------------------------------------------------------------------------------------------------------- #

analysisDataModle = AnalysisDataModle()
# 获取 API json 数据
request_json_data = analysisDataModle.getRequestJson(request_json_file)

# 获取 冰鸟 API 配置 json 数据
bn_config_json_data = analysisDataModle.getRequestJson(bn_config_json_file)
# 获取 发行 API 配置 json 数据
fx_config_json_data = analysisDataModle.getRequestJson(fx_config_json_file)
# 获取 轻度 API 配置 json 数据
qd_config_json_data = analysisDataModle.getRequestJson(qd_config_json_file)

# json_dicts = json.dumps(bn_config_json_data, indent=4)
# print(str(json_dicts))
# exit()

# -------------------------------------------------------------------------------------------------------------------- #

# print('\n---------------------------------- 抓包数据 ----------------------------------')
# print(request_json_data)
print('\n---------------------------------- 开始解析冰鸟接口 ----------------------------------')
# print(fx_config_json_data)

analysisDataModle.analysisApiData('bn', request_json_data, bn_config_json_data)
print('\n---------------------------------- 开始解析发行接口 ----------------------------------')
analysisDataModle.analysisApiData('fx', request_json_data, fx_config_json_data)

# analysisDataModle.analysisApiData('qd', request_json_data, qd_config_json_data)


# 开始解释 API 数据
# analysisDataModle.analysisApiData(request_json_data)

# 开始解析 API 配置文件
# analysisDataModle.analysisApiConfigData(config_json_data)