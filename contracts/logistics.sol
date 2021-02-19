pragma solidity >0.5.0;
pragma experimental ABIEncoderV2;

struct ShipFrom{
    string Name;
    string Address;
    string City;
    string State;
    uint Zip;
    uint SID;
    bool FOB;
    uint userId;
    address userAddress;
}

struct ShipTo{
    string Name;
    string Address;
    string City;
    string State;
    uint Zip;
    uint Location;
    bool FOB;
    uint userId;
    address userAddress;
}

struct Carrier{
    string CarrierName;
    uint TrailerNumber;
    uint SealNumber;
    uint SCAD;//Standard Carrier Alpha Code
    uint ProNumber;
}

struct ThirdPartyDetails{
    string Name;
    string Address;
    string City;
    string State;
    uint Zip;
    uint AppointmentNo;
    string Date;
    string DeliveryInstruction;
}

struct Charges{
    string FreightChargeTerms;
    uint Perpaid;
    uint Collect;
    uint _3rdPartyCharges;
    uint MasterBOL;
}

struct OrderInformation{
    uint OrderNumber;
    uint NumberOfPackage;
    uint Weight;
    uint Pallet;
    uint Cost;
    string AdditionalInformation;
}

struct CarrierInformation{
    uint HandlingUnitQuantity;
    bool HandlingUnitTyoe; //0->pellet, 1->carton
    uint PackageQuantity;
    bool PackageType; //0->pellet, 1->carton
    uint Weight;
    bool HM; //0->not hazardous
    string Description;
    string NMFC;
    string Class;
}

struct TrackingData{
    string date;
    string time;
    //gps data;
    string longitude;
    string latitude;
    string reporterCompanyName;
    bool approved;
    string remarks;
}


struct form{
    
    //-----------------Date Section-------------------------
    string date;

    //-----------------Bill of lading No----------------------
    uint BOL_No;

    
    //-----------------Ship From details-----------------------
    ShipFrom _shipfrom;

    //-----------------Ship To details-----------------------
    ShipTo _shipto;

    //-----------------Customer Order Information----------------------------

    OrderInformation[] _OrderInformationList;
    uint GrandTotalWeight;
    uint GrandTotalPackages;
    uint GrandTotalCost;
    uint creditRemaining;
    //-----------------Payment details-----------------------
    
    bool ifCOD;
    bool ifCheque;
    //payment conditions in setCharges
    
    //-----------------Select shipment agency-------------------------
    uint shipmentAgencyId;
    address shipmentAgencyAddress;
    bool shipmentAgencyApproval; //init to false in contract
    bool inTransit;
    bool delivered;
    bool shipmentApproved;
    bool receiverAcknowledged;
    
    //-----------------Carrier details-----------------------
    Carrier _carrier;
    
    //-----------------3rd Party Freight Charges Bill Section-------------------------
    ThirdPartyDetails _ThirdPartyDetails;
    
    //-----------------Freight Charges---------------------------------------
    Charges _charges;
    

    //-----------------Carrier Information Table------------------------------
    
    CarrierInformation[] _CarrierInformationList;
    
    //-----------------Tracking Data-----------------------------------------
    TrackingData[] _trackingHistory;

}


contract logistics {
    mapping(string=>form) formMap; //shipping id to form
    
    function setDate(string memory shipmentID, string memory _date)public{
        formMap[shipmentID].date = _date;
    }
    
    function getDate(string memory shipmentID) view public returns(string memory){
        return formMap[shipmentID].date;
    }
    
    function setBOL_No(string memory shipmentID, uint _BOL_No)public{
        formMap[shipmentID].BOL_No=_BOL_No;
        formMap[shipmentID].GrandTotalPackages=0;
        formMap[shipmentID].GrandTotalWeight=0;
        formMap[shipmentID].GrandTotalCost = 0;
        formMap[shipmentID].creditRemaining=0;
        formMap[shipmentID].shipmentAgencyApproval = false;
        formMap[shipmentID].inTransit = false;
        formMap[shipmentID].delivered = false;
        formMap[shipmentID].shipmentApproved=false;
        formMap[shipmentID].receiverAcknowledged = false;
    }
    
    function getBOL_No(string memory shipmentID)view public returns(uint){
        return(formMap[shipmentID].BOL_No);
    }
    
    function setShipFrom(string memory shipmentID, string memory _Name,string memory _Address,string memory _City,string memory _State,uint _Zip,uint _SID,bool _FOB, uint _userId, address _userAddress)public{
        formMap[shipmentID]._shipfrom.Name=_Name;
        formMap[shipmentID]._shipfrom.Address=_Address;
        formMap[shipmentID]._shipfrom.City=_City;
        formMap[shipmentID]._shipfrom.State=_State;
        formMap[shipmentID]._shipfrom.Zip=_Zip;
        formMap[shipmentID]._shipfrom.SID=_SID;
        formMap[shipmentID]._shipfrom.FOB=_FOB;
        formMap[shipmentID]._shipfrom.userId = _userId;
        formMap[shipmentID]._shipfrom.userAddress = _userAddress;
    }
    
    function getShipFrom(string memory shipmentID)view public returns(ShipFrom memory){
        return(formMap[shipmentID]._shipfrom);
    }
    
    function setShipTo(string memory shipmentID, string memory _Name,string memory _Address,string memory _City,string memory _State,uint _Zip, uint _Location,bool _FOB, uint _userId, address _userAddress)public{
        formMap[shipmentID]._shipto.Name=_Name;
        formMap[shipmentID]._shipto.Address=_Address;
        formMap[shipmentID]._shipto.City=_City;
        formMap[shipmentID]._shipto.State=_State;
        formMap[shipmentID]._shipto.Zip=_Zip;
        formMap[shipmentID]._shipto.Location=_Location;
        formMap[shipmentID]._shipto.FOB=_FOB;
        formMap[shipmentID]._shipto.userId = _userId;
        formMap[shipmentID]._shipto.userAddress = _userAddress;
    }
    
    function getShipTo(string memory shipmentID) view public returns(ShipTo memory){
        return(formMap[shipmentID]._shipto);
    }
    
    function setOrderInformation(string memory shipmentID, uint _OrderNumber,uint _NumberOfPackage,uint _Weight,uint _Pallet,string memory _AdditionalInformation, uint _Cost)public{
        OrderInformation memory _OrderInformation;
        _OrderInformation.OrderNumber=_OrderNumber;
        _OrderInformation.NumberOfPackage=_NumberOfPackage;
        _OrderInformation.Weight=_Weight;
        _OrderInformation.Pallet=_Pallet;
        _OrderInformation.Cost = _Cost;
        _OrderInformation.AdditionalInformation=_AdditionalInformation;
        formMap[shipmentID]._OrderInformationList.push(_OrderInformation);
        formMap[shipmentID].GrandTotalWeight+=_OrderInformation.Weight;
        formMap[shipmentID].GrandTotalPackages+=_OrderInformation.NumberOfPackage;
        formMap[shipmentID].GrandTotalCost+=_Cost;
        formMap[shipmentID].creditRemaining+=_Cost;
    }

    function getOrderInformation(string memory shipmentID)view public returns (OrderInformation[] memory){
        return formMap[shipmentID]._OrderInformationList;
    }
    
    function getGrandTotal(string memory shipmentID) view public returns(uint, uint, uint){
        return(formMap[shipmentID].GrandTotalWeight, formMap[shipmentID].GrandTotalPackages, formMap[shipmentID].GrandTotalCost);
    }
    
    //function setPaymentInformation().....
    
    //function getPaymentInformation().....
    
    function setShipmentAgency(string memory shipmentID, uint _shipmentAgencyId, address _shipmentAgencyAddress) public{
        formMap[shipmentID].shipmentAgencyId = _shipmentAgencyId;
        formMap[shipmentID].shipmentAgencyAddress = _shipmentAgencyAddress;
    }
    
    function getShipmentAgency(string memory shipmentID) view public returns(uint, address) {
        return (formMap[shipmentID].shipmentAgencyId, formMap[shipmentID].shipmentAgencyAddress);
    }
    

    function setCarrier(string memory shipmentID, string memory _CarrierName,uint _TrailerNumber,uint _SealNumber,uint _SCAD,uint _ProNumber) public{
        
        //make shipmentAgencyApproval true here 
        
        formMap[shipmentID]._carrier.CarrierName=_CarrierName;
        formMap[shipmentID]._carrier.TrailerNumber=_TrailerNumber;
        formMap[shipmentID]._carrier.SealNumber=_SealNumber;
        formMap[shipmentID]._carrier.SCAD=_SCAD;
        formMap[shipmentID]._carrier.ProNumber=_ProNumber;
    }
    
    function getCarrier(string memory shipmentID) view public returns(Carrier memory){
        return(formMap[shipmentID]._carrier);
    }
    
    function setThirdPartyDetails(string memory shipmentID, string memory _Name,string memory _Address,string memory _City,string memory _State,uint _Zip,uint _AppointmentNo,string  memory _Date,string memory _DeliveryInstruction )public{
        formMap[shipmentID]._ThirdPartyDetails.Name=_Name;
        formMap[shipmentID]._ThirdPartyDetails.Address=_Address;
        formMap[shipmentID]._ThirdPartyDetails.City=_City;
        formMap[shipmentID]._ThirdPartyDetails.State=_State;
        formMap[shipmentID]._ThirdPartyDetails.Zip=_Zip;
        formMap[shipmentID]._ThirdPartyDetails.AppointmentNo=_AppointmentNo;
        formMap[shipmentID]._ThirdPartyDetails.Date=_Date;
        formMap[shipmentID]._ThirdPartyDetails.DeliveryInstruction=_DeliveryInstruction;
    }
    
    function getThirdPartyDetails(string memory shipmentID) view public returns(ThirdPartyDetails memory){
        return(formMap[shipmentID]._ThirdPartyDetails);
    }
    
    function setCharges(string memory shipmentID, string memory _FreightChargeTerms,uint _Perpaid,uint _Collect,uint __3rdPartyCharges,uint _MasterBOL)public{
        formMap[shipmentID]._charges.FreightChargeTerms=_FreightChargeTerms;
        formMap[shipmentID]._charges.Perpaid=_Perpaid;
        formMap[shipmentID]._charges.Collect=_Collect;
        formMap[shipmentID]._charges._3rdPartyCharges=__3rdPartyCharges;
        formMap[shipmentID]._charges.MasterBOL=_MasterBOL;
    }
    
    function getCharges(string memory shipmentID)view public returns(Charges memory){
        return(formMap[shipmentID]._charges);
    }
    
    function setCarrierInformation(string memory shipmentID, uint _HandlingUnitQuantity, bool _HandlingUnitTyoe, uint _PackageQuantity, bool _PackageType,
                                uint _Weight, bool _HM, string memory _Description, string memory _NMFC, string memory _Class) public {
    
        CarrierInformation memory _CarrierInformation;
        _CarrierInformation.HandlingUnitTyoe = _HandlingUnitTyoe;
        _CarrierInformation.HandlingUnitQuantity = _HandlingUnitQuantity;
        _CarrierInformation.PackageQuantity = _PackageQuantity;
        _CarrierInformation.PackageType = _PackageType;
        _CarrierInformation.Weight = _Weight;
        _CarrierInformation.HM = _HM;
        _CarrierInformation.Description = _Description;
        _CarrierInformation.NMFC = _NMFC;
        _CarrierInformation.Class = _Class;
        formMap[shipmentID]._CarrierInformationList.push(_CarrierInformation);
    }
    
    function getCarrierInformation(string memory shipmentID) view public returns(CarrierInformation[] memory) {
        return formMap[shipmentID]._CarrierInformationList;
    }
    
    function setTrackingData(string memory shipmentID, string memory _date, string memory _time, string memory _longitude, string memory _latitude, string memory _reporterCompanyName, bool _approved, string memory _remarks) public{
        TrackingData memory _trackingData;
        _trackingData.date = _date;
        _trackingData.time = _time;
        _trackingData.longitude = _longitude;
        _trackingData.latitude = _latitude;
        _trackingData.reporterCompanyName = _reporterCompanyName;
        _trackingData.approved = _approved;
        _trackingData.remarks = _remarks;
        formMap[shipmentID]._trackingHistory.push(_trackingData);
    }
    
    function getTrackingData(string memory shipmentID) view public returns(TrackingData[] memory) {
        return formMap[shipmentID]._trackingHistory;
    }
    
    function getOrderSnapshot(string memory shipmentID) view public returns(string memory, string memory, bool, uint , uint){
        string memory shipFrom = formMap[shipmentID]._shipfrom.Name;
        string memory shipTo = formMap[shipmentID]._shipto.Name;
        bool approved = formMap[shipmentID].receiverAcknowledged;
        uint cost = formMap[shipmentID].GrandTotalCost;
        uint creditRemaining = formMap[shipmentID].creditRemaining;
        
        return (shipFrom, shipTo, approved, cost, creditRemaining);
    }
    
    function getScanDetails(string memory shipmentID) view public returns(uint, uint, string memory, string memory, string memory, uint) {
        uint weight = formMap[shipmentID].GrandTotalWeight;
        uint packages = formMap[shipmentID].GrandTotalPackages;
        string memory shipFrom = formMap[shipmentID]._shipfrom.Name;
        string memory shipTo = formMap[shipmentID]._shipto.Name;
        string memory shipToCity = formMap[shipmentID]._shipto.City;
        uint costremaining = formMap[shipmentID].creditRemaining;
        
        return (weight, packages, shipFrom, shipTo, shipToCity, costremaining);
        
    }
    
    function payEther(string memory shipmentID) public payable {
        formMap[shipmentID].creditRemaining-=msg.value;
    }
    
    function recievePayment(string memory shipmentID, uint amount) public{
        formMap[shipmentID].creditRemaining -= amount;
        formMap[shipmentID].receiverAcknowledged = true;
    }
    
}