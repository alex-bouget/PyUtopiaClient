from ..System.LoadingSystem import LoadingSys


class BattleStartCanvas(LoadingSys):
    def __init__(self, master, lib):
        super().__init__(master)
        self.Lib = lib
        self.deck = []

    def start(self, battle_url_server, player_id, version, deck):
        self.Lib.StartBattle(battle_url_server, player_id, version)
        self.deck = deck
        self.wr.set("Loading...")
        self.after(500, self.loop1)

    def loop1(self):
        data = self.Lib.BattleServer.Get()
        if data is None:
            self.after(500, self.loop1)
        elif data == "BattleServer.Server.Full":
            print("wut")
        elif data == "BattleServer.Server.Wait":
            self.Lib.BattleServer.WaitServer()
            self.loop2()

    def loop2(self):
        data = self.Lib.BattleServer.Get()
        if data is None:
            self.after(500, self.loop2)
        elif data in ["BattleServer.Server.Bdd_Problem", "BattleServer.Server.Client_Problem"]:
            print("wut")
        elif data == "BattleServer.Server.Wait_Player":
            self.Lib.BattleServer.WaitServer()
            self.after(500, self.loop2)
        else:
            self.Starter = data.split(".")[-1]
            self.Lib.BattleServer.SendDeck(self.deck)
            self.loop3()

    def loop3(self):
        data = self.Lib.BattleServer.Get()
        if data is None:
            self.after(500, self.loop3)
        else:
            self.ret = data
            self.StartFinish = True