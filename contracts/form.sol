pragma solidity >0.5.0;
pragma experimental ABIEncoderV2;

contract form{
    
    //-----------------Date Section-------------------------
    string date;
    function setDate(string memory _date)public{
        date=_date;
    }
    function getDate()view public returns(string memory){
        return(date);
    }
    //-----------------Bill of lading No----------------------
    uint BOL_No;
    function setBOL_No(uint _BOL_No)public{
        BOL_No=_BOL_No;
    }
    function getBOL_No()view public returns(uint){
        return(BOL_No);
    }
    
    //-----------------Ship From details-----------------------
    struct ShipFrom{
        string Name;
        string Address;
        string City;
        string State;
        uint Zip;
        uint SID;
        bool FOB;
    }ShipFrom _shipfrom;
    function setShipFrom(string memory _Name,string memory _Address,string memory _City,string memory _State,uint _Zip,uint _SID,bool _FOB)public{
        _shipfrom.Name=_Name;
        _shipfrom.Address=_Address;
        _shipfrom.City=_City;
        _shipfrom.State=_State;
        _shipfrom.Zip=_Zip;
        _shipfrom.SID=_SID;
        _shipfrom.FOB=_FOB;
    }
    function getShipFrom()view public returns(ShipFrom memory){
        return(_shipfrom);
    }
    
    //-----------------Ship To details-----------------------
    struct ShipTo{
        string Name;
        string Address;
        string City;
        string State;
        uint Zip;
        uint Location;
        bool FOB;
    }ShipTo _shipto;
    function setShipTo(string memory _Name,string memory _Address,string memory _City,string memory _State,uint _Zip, uint _Location,bool _FOB)public{
        _shipto.Name=_Name;
        _shipto.Address=_Address;
        _shipto.City=_City;
        _shipto.State=_State;
        _shipto.Zip=_Zip;
        _shipto.Location=_Location;
        _shipto.FOB=_FOB;
    }
    function getShipTo() view public returns(ShipTo memory){
        return(_shipto);
    }
    //-----------------Carrier details-----------------------
    struct Carrier{
        string CarrierName;
        uint TrailerNumber;
        uint SealNumber;
        uint SCAD;//Standard Carrier Alpha Code
        uint ProNumber;
    }Carrier _carrier;
    
    function setCarrier(string memory _CarrierName,uint _TrailerNumber,uint _SealNumber,uint _SCAD,uint _ProNumber) public{
        _carrier.CarrierName=_CarrierName;
        _carrier.TrailerNumber=_TrailerNumber;
        _carrier.SealNumber=_SealNumber;
        _carrier.SCAD=_SCAD;
        _carrier.ProNumber=_ProNumber;
    }
    function getCarrier() view public returns(Carrier memory){
        return(_carrier);
    }
    
    //-----------------3rd Party Freight Charges Bill Section-------------------------
    struct ThirdPartyDetails{
        string Name;
        string Address;
        string City;
        string State;
        uint Zip;
        uint AppointmentNo;
        string Date;
        string DeliveryInstruction;
    }ThirdPartyDetails _ThirdPartyDetails;
    
    function setThirdPartyDetails(string memory _Name,string memory _Address,string memory _City,string memory _State,uint _Zip,uint _AppointmentNo,string  memory _Date,string memory _DeliveryInstruction )public{
        _ThirdPartyDetails.Name=_Name;
        _ThirdPartyDetails.Address=_Address;
        _ThirdPartyDetails.City=_City;
        _ThirdPartyDetails.State=_State;
        _ThirdPartyDetails.Zip=_Zip;
        _ThirdPartyDetails.AppointmentNo=_AppointmentNo;
        _ThirdPartyDetails.Date=_Date;
        _ThirdPartyDetails.DeliveryInstruction=_DeliveryInstruction;
    }
    
    function getThirdPartyDeatails() view public returns(ThirdPartyDetails memory){
        return(_ThirdPartyDetails);
    }
    
    //-----------------Freight Charges---------------------------------------
    struct Charges{
        string FreightChargeTerms;
        uint Perpaid;
        uint Collect;
        uint _3rdPartyCharges;
        uint MasterBOL;
    }Charges _charges;
    
    function setCharges(string memory _FreightChargeTerms,uint _Perpaid,uint _Collect,uint __3rdPartyCharges,uint _MasterBOL)public{
        _charges.FreightChargeTerms=_FreightChargeTerms;
        _charges.Perpaid=_Perpaid;
        _charges.Collect=_Collect;
        _charges._3rdPartyCharges=__3rdPartyCharges;
        _charges.MasterBOL=_MasterBOL;
    }
    
    function getCharges()view public returns(Charges memory){
        return(_charges);
    }
    //-----------------Customer Order Information----------------------------
    struct OrderInformation{
        uint OrderNumber;
        uint NumberOfPackage;
        uint Weight;
        uint Pallet;
        string AdditionalInformation;
    }mapping(uint=>OrderInformation) _OrderInformation;
    uint[]  count ;
    
    function setOrderInformation(uint Index,uint _OrderNumber,uint _NumberOfPackage,uint _Weight,uint _Pallet,string memory _AdditionalInformation)public{
        _OrderInformation[Index].OrderNumber=_OrderNumber;
        _OrderInformation[Index].NumberOfPackage=_NumberOfPackage;
        _OrderInformation[Index].Weight=_Weight;
        _OrderInformation[Index].Pallet=_Pallet;
        _OrderInformation[Index].AdditionalInformation=_AdditionalInformation;
        count.push(Index);
    }
    
    function row(uint index) view public returns(OrderInformation memory){
        return(_OrderInformation[index]);
    }
    
    
    function getOrderInformation() public{
        uint len=count.length;
        for(uint i=0;i<len;i++){
            row(i);
        }
    }
    
    uint GrandTotal;
    function setGrandTotal(uint _GrandTotal) public{
        GrandTotal=_GrandTotal;
    }
    function getGrandTotal() view public returns(uint){
        return(GrandTotal);
    }
}


