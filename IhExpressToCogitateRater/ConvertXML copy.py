import os

ihExpessXML = os.path.join("./IHExpressRqXml", "000050400.xml")
cogitateXML = os.path.join("./../NewRater/NewRater/App_Data", "SGIH-GAPPA.xml")


taglist = []


def readXML():
    policyEndTag = True

    signInTag = """<SignIn>
      <LoginName>admin</LoginName>
      <Password>admin</Password>
      <RequestVersion>1.0.0.0</RequestVersion>
      <RaterVersion>2.0.0.0</RaterVersion>
      <RulesVersion>2.0.0.0</RulesVersion>
      <RequesteDateTime>2017-12-17 08:11:30.154</RequesteDateTime>
      <ReferenceQuoteId>2710</ReferenceQuoteId>
      <ShowPremium>Y</ShowPremium>
      <ShowDeductibles>N</ShowDeductibles>
      <ShowDesc>Y</ShowDesc>
      <ShowResult>Y</ShowResult>
      <ShowSteps>N</ShowSteps>
      <ShowVar>Y</ShowVar>
      <ShowRateBasis>N</ShowRateBasis>
      <ShowPremiumSteps>N</ShowPremiumSteps>
      <ShowDetailLevelTotalPrem>Y</ShowDetailLevelTotalPrem>
      <RulesState>GAPA</RulesState>
      <RaterUrl>https://rater.cogitate.us/api/rater</RaterUrl>
      <ProductCode>PPA</ProductCode>
      <CoverHolder>IH.AutoRaterMigration</CoverHolder>
   </SignIn>"""


    f = open(ihExpessXML, "r")
    for line in f:        
        line = line.replace("\n","")         
        if "ibdoc" in line:
            line = line.replace("ibdoc","Rater")
        if "<m" in line:
            line = line.replace("<m","<Parameter")
            line = line.replace("n=","code=")
            line = line.replace("/>","</Parameter>")
            line = line.replace(' v="',">")
            line = line.replace('"</',"</")
        if "desc=" in line:
            line = line.replace('desc=',"code=")
            line = line.replace('<c',"<Parameter")
        if "</c>" in line:
            line = line.replace('</c>',"</Parameter>")
        if "<rate lob=" in line:
            line = "<RateParameter>"
        if "</rate>" in line:
            line = "</RateParameter>"
        taglist.append(line)
        
    print("##############################################")

    fwrite= open(cogitateXML,"w+")

    for i in range(len(taglist)):
        if("<Rater>" in taglist[i]):
            print(taglist[i])
            fwrite.write(taglist[i]+"\n")
            print(signInTag)
            fwrite.write(signInTag+"\n")
        elif('code="Policy"' in taglist[i]):
            print("")
            fwrite.write("\n")
        elif(policyEndTag and 'code="Driver"' in taglist[i+1]):
            policyEndTag = False
            print("")            
            fwrite.write("\n")
        elif(">" in taglist[i]):
            print(taglist[i].replace("/>","></Parameter>"))
            fwrite.write(taglist[i].replace("/>","></Parameter>")+"\n")
        else:
            fwrite.write(taglist[i]+"\n")
	        # print(taglist[i])
            
        
    f.close
    fwrite.close


readXML()