from elasticsearch import Elasticsearch
import json

es = Elasticsearch([{'host':'localhost','port':9200}])  #启动ES
data = {"name": "小明", "age": "8", "gender": "男"}
res = es.index(index="cggg", doc_type="doc", body=data)

# data2 = {"name": "小方", "age": "9", "gender": "女"}
# res = es.index(index="cggg", doc_type="doc", body=data2)

# es.indices.delete(index='stocks')

# body = {
#     "query":{
#         "match_all":{}
#     }
# }

# body = {
#     "query":{
#         "term":{
#             "any":"data01"
#         }
#     }
# }

with open(r'C:\Users\Administrator\Desktop\爬虫\2.json','r',encoding='utf-8')as fp:
    body = json.load(fp)
    # print(body['query']['term']['华夏成长混合'])
#     body = {
# "华夏成长混合": {"中国平安": "6.04%", "南极电商": "5.90%", "中南建设": "5.30%", "贵州茅台": "5.01%", "东方雨虹": "4.57%", "保利地产": "4.30%", "航天发展": "4.14%", "中航机电": "3.78%", "丽珠集团": "2.90%", "五 粮 液": "2.86%", "18国开": "3.55%", "20国开": "2.50%", "19进出": "2.30%", "15华能": "2.09%", "20进出": "2.08%", "0": "0"}, 
# "中海可转债债券A": {"东方财富": "6.50%", "中信证券": "4.85%", "财通证券": "3.48%", "海通证券": "2.23%", "华泰证券": "1.94%", "兴业银行": "1.28%", "长证转债": "24.36%", "光大转债": "23.67%", "国君转债": "22.89%", "苏银转债": "13.66%", "浦发转债": "7.30%", "0": "0"}
# }
    # print(body)
    es.index(index="all_stocks",body=body)
    # 查询name="python"的所有数据

    # find = {
    # "query": {
    #     "match" : {
    #         "doc.name":"华夏成长混合"
    #     }
    # }
    # }

    # answer = es.search(index="all_stocks",body=find)
    # print(answer['hits']['hits'][0]['_source'])
    # print(answer['hits'])
    # answer = es.get(index='stocks', id='南极电商')
    # print(answer)