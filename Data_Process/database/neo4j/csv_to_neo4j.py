import pandas as pd
from neo4j import GraphDatabase

# 连接到 Neo4j 数据库
uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"  #

driver = GraphDatabase.driver(uri, auth=(user, password))

# 读取 CSV 文件
df = pd.read_csv('../../output_data/output.csv')

# 用于存储上一级节点的字典
last_nodes = {
    'Level 1': None,
    'Level 2': None,
    'Level 3': None,
    'Level 4': None
}

# 用于记录同级内容的上一个节点
content_sequence = []

# 创建节点
def create_nodes(tx, level, name):
    query = f"""
    MERGE (n:{level} {{name: $name}})
    RETURN n
    """
    tx.run(query, name=name)

# 创建关系
def create_relationship(tx, parent_level, parent_name, child_level, child_name, rel_type):
    query = f"""
    MATCH (parent:{parent_level} {{name: $parent_name}})
    MERGE (child:{child_level} {{name: $child_name}})
    MERGE (parent)-[r:{rel_type}]->(child)
    """
    tx.run(query, parent_name=parent_name, child_name=child_name)

with driver.session() as session:
    # 清空数据库，导入数据量不大的情况下可以使用，数据量较大的时候最好注释
    session.execute_write(lambda tx: tx.run("MATCH (n) DETACH DELETE n"))

    for index, row in df.iterrows():
        level_names = {}
        for level in ['Level 1', 'Level 2', 'Level 3', 'Level 4']:
            if pd.notna(row[level]):  # 非空检测
                level_names[level] = row[level]
            else:
                level_names[level] = None

        # 创建节点和关系
        if level_names['Level 1']:  # 首节点，一般为章节
            session.execute_write(create_nodes, 'Chapter', level_names['Level 1']) # 回调函数，标签，内容
            last_nodes['Level 1'] = level_names['Level 1']
            last_nodes['Level 2'] = None
            last_nodes['Level 3'] = None
            last_nodes['Level 4'] = None

        if level_names['Level 2']:  # 首节点和二节点的联系
            session.execute_write(create_relationship, 'Chapter', last_nodes['Level 1'], 'Section', level_names['Level 2'], 'HAS_SECTION')
            last_nodes['Level 2'] = level_names['Level 2']
            last_nodes['Level 3'] = None
            last_nodes['Level 4'] = None

        if level_names['Level 3']:  # 二节点和三节点的联系
            session.execute_write(create_relationship, 'Section', last_nodes['Level 2'], 'Subsection', level_names['Level 3'], 'HAS_SUBSECTION')
            last_nodes['Level 3'] = level_names['Level 3']
            last_nodes['Level 4'] = None
            content_sequence = []  # 重置内容序列

        if level_names['Level 4']:
            # 创建内容节点
            session.execute_write(create_relationship, 'Subsection', last_nodes['Level 3'], 'Content', level_names['Level 4'], 'HAS_CONTENT')
            # 处理内容顺序
            if content_sequence:
                # 创建顺序关系
                query = """
                MATCH (prev:Content {name: $prev_content})
                MATCH (current:Content {name: $current_content})
                MERGE (prev)-[:NEXT]->(current)
                """
                session.run(query, prev_content=content_sequence[-1], current_content=level_names['Level 4'])
            content_sequence.append(level_names['Level 4'])

driver.close()
