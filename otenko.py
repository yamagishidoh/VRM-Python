import vrmapi
LAYOUT = vrmapi.LAYOUT()
IMGUI = vrmapi.ImGui()

skytexture_id = [0]
skytexturedict = {5:'ID5 big空＆雲', 6:'ID6 zioリング', 7:'ID7 zio火星'}
weathertype = [0]
weatherdict = {0:'晴れ', 1:'雨', 2:'雪'}
suntype = [0]
sundict = {0:'昼間', 1:'朝日', 2:'夕日', 3:'夜間', 4:'曇り', 5:'夕暮れ', 6:'夕日2'}
fogtype = [0]
fogdict = {0:'標準', 1:'都市', 2:'山岳', 3:'朝霧', 4:'濃霧', 5:'郊外'}
fog_amount = 1.0
fog_amount_list = [1.0]

def vrmevent_ex(obj,ev,param):
    if ev == 'init':
        obj.SetEventFrame()
    elif ev == 'broadcast':
        dummy = 1
    elif ev == 'timer':
        dummy = 1
    elif ev == 'time':
        dummy = 1
    elif ev == 'after':
        dummy = 1
    elif ev == 'frame':
        gui_otenkokun()
    elif ev == 'keydown':
        dummy = 1

def gui_otenkokun():
    global skytexture_id
    global weathertype
    global suntype
    global fogype
    global fog_amount
    global fog_amount_list
    global key2
    IMGUI.Begin('otenkokun_window', 'お天候くん')
    IMGUI.Text("天球テクスチャー")
    for key, name in skytexturedict.items():
        IMGUI.SameLine()
        if IMGUI.RadioButton('btnskytexture{}'.format(key), name, skytexture_id, key):
            LAYOUT.SKY().SetSkyFactor(1.0)
            LAYOUT.SKY().LoadSkyImage(0, key)
            LAYOUT.SKY().SetSkyFactor(0.0)
    IMGUI.Text("天気")
    for key, name in weatherdict.items():
        IMGUI.SameLine()
        if IMGUI.RadioButton('btnweather{}'.format(key), name, weathertype, key):
            LAYOUT.SKY().SetWeather(key)
    IMGUI.Separator()
    IMGUI.Text("太陽光")
    for key, name in sundict.items():
        IMGUI.SameLine()
        if IMGUI.RadioButton('btnsun{}'.format(key), name, suntype, key):
            LAYOUT.SKY().SetSunType(key, 1)
    IMGUI.Separator()
    IMGUI.Text("フォグの種類")
    for key, name in fogdict.items():
        IMGUI.SameLine()
        if IMGUI.RadioButton('btnfog{}'.format(key), name, fogtype, key):
            LAYOUT.SKY().SetFog(key, fog_amount, 1)
            key2 = key
    if IMGUI.SliderFloat('fogslider', '霧の量', fog_amount_list, 0.0, 1.0):
        float("fog_amount_list")
        LAYOUT.SKY().SetFog(key2, fog_amount_list, 1)
    IMGUI.End()