"""谱牒（PUDIE）· 资产分类谱系

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：资产分类谱系。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Pudie:
    """谱牒（PUDIE）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "PUDIE"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.tree = {}
        self._seq = 0

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "pudie",
            "cn": "谱牒",
            "code": self.CODE,
            "duty": "资产分类谱系",
            "mingwen": "正本溯源，分类归宗",
            "anchor": self.ANCHOR,
        }

    def classify(self, asset):
        """正本溯源，分类归宗。"""
        self._seq += 1
        aid = (asset or {}).get("id") or "PD-%04d" % self._seq
        self.tree[aid] = {"kind": (asset or {}).get("kind", "generic"),
                          "parent": (asset or {}).get("parent")}
        self.events.append({"event": "classify", "asset_id": aid})
        return {"asset_id": aid, "kind": self.tree[aid]["kind"], "parent": self.tree[aid]["parent"]}

    def lineage(self, asset_id):
        """沿谱系上溯至宗。"""
        if asset_id not in self.tree:
            raise KeyError("谱牒无此号： %s" % asset_id)
        chain = []
        cur = asset_id
        while cur is not None:
            chain.append(cur)
            cur = self.tree[cur]["parent"]
        return chain
