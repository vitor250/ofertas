import json,sys,time,urllib.parse,urllib.request,datetime
K=open("/Users/vitorhugo/Desktop/ofertas/1-BR/escalalow/.chave").read().strip()
H=datetime.datetime(2026,10,30,tzinfo=datetime.timezone.utc)
Q=[l.strip().split("|") for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")]
out={};used=0
for c,t in Q:
    ads=[];tok=None;total=None
    for _ in range(2):
        p=dict(engine="meta_ad_library",active_status="active",search_type="keyword_exact_phrase",q=t,country=c,api_key=K)
        if tok:p["next_page_token"]=tok
        d=None
        for tent in range(8):
            try:d=json.loads(urllib.request.urlopen("https://www.searchapi.io/api/v1/search?"+urllib.parse.urlencode(p),timeout=40).read());break
            except Exception as e:time.sleep(12+tent*6)
        if d is None:print("ERRO",c,t,flush=True);break
        used+=1;total=total or d.get("search_information",{}).get("total_results");ads+=d.get("ads",[]);tok=(d.get("pagination") or {}).get("next_page_token")
        if not tok:break
        time.sleep(.3)
    pg={}
    for a in ads:
        sd=a.get("start_date")
        if not sd:continue
        dias=(H-datetime.datetime.fromisoformat(sd.replace("Z","+00:00"))).days;s=a.get("snapshot") or {}
        o=pg.setdefault(a["page_id"],{"page":a.get("page_name",""),"id":a["page_id"],"dias":0,"n":0,"link":"","txt":"","cur":a.get("currency") or s.get("currency") or ""})
        o["n"]+=a.get("collation_count") or 1
        if dias>o["dias"]:o.update(dias=dias,link=s.get("link_url") or "",txt=((s.get("body") or {}).get("text") or s.get("title") or "")[:110].replace("\n"," "))
    L=sorted(pg.values(),key=lambda o:-o["dias"])
    bons=[o for o in L if o["dias"]>=30 and o["n"]>=3]
    out[c+"|"+t]={"total":total,"lidos":len(ads),"top":L[:6],"bons":bons}
    print(f"[{c}] {t}: tot={total} lidos={len(ads)} bons30d/3cr={len(bons)}",flush=True)
    for o in L[:4]:print(f"   {o['dias']}d {o['n']}cr {o['page'][:30]}|{o['link'][:45]}|{o['txt'][:70]}",flush=True)
    json.dump(out,open(sys.argv[1]+".json","w"),ensure_ascii=False,indent=1)
print("creditos",used)
