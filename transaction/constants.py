contractAddress= '0xbDa6A2F91Fb70174007164421c5a6F093f5f6499'
abi = '[{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"}],"name":"getBOL_No","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"}],"name":"getCarrier","outputs":[{"components":[{"internalType":"string","name":"CarrierName","type":"string"},{"internalType":"uint256","name":"TrailerNumber","type":"uint256"},{"internalType":"uint256","name":"SealNumber","type":"uint256"},{"internalType":"uint256","name":"SCAD","type":"uint256"},{"internalType":"uint256","name":"ProNumber","type":"uint256"}],"internalType":"struct Carrier","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"}],"name":"getCarrierInformation","outputs":[{"components":[{"internalType":"uint256","name":"HandlingUnitQuantity","type":"uint256"},{"internalType":"bool","name":"HandlingUnitTyoe","type":"bool"},{"internalType":"uint256","name":"PackageQuantity","type":"uint256"},{"internalType":"bool","name":"PackageType","type":"bool"},{"internalType":"uint256","name":"Weight","type":"uint256"},{"internalType":"bool","name":"HM","type":"bool"},{"internalType":"string","name":"Description","type":"string"},{"internalType":"string","name":"NMFC","type":"string"},{"internalType":"string","name":"Class","type":"string"}],"internalType":"struct CarrierInformation[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"}],"name":"getCharges","outputs":[{"components":[{"internalType":"string","name":"FreightChargeTerms","type":"string"},{"internalType":"uint256","name":"Perpaid","type":"uint256"},{"internalType":"uint256","name":"Collect","type":"uint256"},{"internalType":"uint256","name":"_3rdPartyCharges","type":"uint256"},{"internalType":"uint256","name":"MasterBOL","type":"uint256"}],"internalType":"struct Charges","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"}],"name":"getDate","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"}],"name":"getGrandTotal","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"}],"name":"getOrderInformation","outputs":[{"components":[{"internalType":"uint256","name":"OrderNumber","type":"uint256"},{"internalType":"uint256","name":"NumberOfPackage","type":"uint256"},{"internalType":"uint256","name":"Weight","type":"uint256"},{"internalType":"uint256","name":"Pallet","type":"uint256"},{"internalType":"string","name":"AdditionalInformation","type":"string"}],"internalType":"struct OrderInformation[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"}],"name":"getOrderSnapshot","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"bool","name":"","type":"bool"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"}],"name":"getScanDetails","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"}],"name":"getShipFrom","outputs":[{"components":[{"internalType":"string","name":"Name","type":"string"},{"internalType":"string","name":"Address","type":"string"},{"internalType":"string","name":"City","type":"string"},{"internalType":"string","name":"State","type":"string"},{"internalType":"uint256","name":"Zip","type":"uint256"},{"internalType":"uint256","name":"SID","type":"uint256"},{"internalType":"bool","name":"FOB","type":"bool"},{"internalType":"uint256","name":"userId","type":"uint256"},{"internalType":"address","name":"userAddress","type":"address"}],"internalType":"struct ShipFrom","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"}],"name":"getShipTo","outputs":[{"components":[{"internalType":"string","name":"Name","type":"string"},{"internalType":"string","name":"Address","type":"string"},{"internalType":"string","name":"City","type":"string"},{"internalType":"string","name":"State","type":"string"},{"internalType":"uint256","name":"Zip","type":"uint256"},{"internalType":"uint256","name":"Location","type":"uint256"},{"internalType":"bool","name":"FOB","type":"bool"},{"internalType":"uint256","name":"userId","type":"uint256"},{"internalType":"address","name":"userAddress","type":"address"}],"internalType":"struct ShipTo","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"}],"name":"getShipmentAgency","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"}],"name":"getThirdPartyDetails","outputs":[{"components":[{"internalType":"string","name":"Name","type":"string"},{"internalType":"string","name":"Address","type":"string"},{"internalType":"string","name":"City","type":"string"},{"internalType":"string","name":"State","type":"string"},{"internalType":"uint256","name":"Zip","type":"uint256"},{"internalType":"uint256","name":"AppointmentNo","type":"uint256"},{"internalType":"string","name":"Date","type":"string"},{"internalType":"string","name":"DeliveryInstruction","type":"string"}],"internalType":"struct ThirdPartyDetails","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"}],"name":"getTrackingData","outputs":[{"components":[{"internalType":"string","name":"date","type":"string"},{"internalType":"string","name":"time","type":"string"},{"internalType":"string","name":"longitude","type":"string"},{"internalType":"string","name":"latitude","type":"string"},{"internalType":"string","name":"reporterCompanyName","type":"string"},{"internalType":"bool","name":"approved","type":"bool"},{"internalType":"string","name":"remarks","type":"string"}],"internalType":"struct TrackingData[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"}],"name":"payEther","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"recievePayment","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"},{"internalType":"uint256","name":"_BOL_No","type":"uint256"}],"name":"setBOL_No","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"},{"internalType":"string","name":"_CarrierName","type":"string"},{"internalType":"uint256","name":"_TrailerNumber","type":"uint256"},{"internalType":"uint256","name":"_SealNumber","type":"uint256"},{"internalType":"uint256","name":"_SCAD","type":"uint256"},{"internalType":"uint256","name":"_ProNumber","type":"uint256"}],"name":"setCarrier","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"},{"internalType":"uint256","name":"_HandlingUnitQuantity","type":"uint256"},{"internalType":"bool","name":"_HandlingUnitTyoe","type":"bool"},{"internalType":"uint256","name":"_PackageQuantity","type":"uint256"},{"internalType":"bool","name":"_PackageType","type":"bool"},{"internalType":"uint256","name":"_Weight","type":"uint256"},{"internalType":"bool","name":"_HM","type":"bool"},{"internalType":"string","name":"_Description","type":"string"},{"internalType":"string","name":"_NMFC","type":"string"},{"internalType":"string","name":"_Class","type":"string"}],"name":"setCarrierInformation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"},{"internalType":"string","name":"_FreightChargeTerms","type":"string"},{"internalType":"uint256","name":"_Perpaid","type":"uint256"},{"internalType":"uint256","name":"_Collect","type":"uint256"},{"internalType":"uint256","name":"__3rdPartyCharges","type":"uint256"},{"internalType":"uint256","name":"_MasterBOL","type":"uint256"}],"name":"setCharges","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"},{"internalType":"string","name":"_date","type":"string"}],"name":"setDate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"},{"internalType":"uint256","name":"_OrderNumber","type":"uint256"},{"internalType":"uint256","name":"_NumberOfPackage","type":"uint256"},{"internalType":"uint256","name":"_Weight","type":"uint256"},{"internalType":"uint256","name":"_Pallet","type":"uint256"},{"internalType":"string","name":"_AdditionalInformation","type":"string"},{"internalType":"uint256","name":"_Cost","type":"uint256"}],"name":"setOrderInformation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"},{"internalType":"string","name":"_Name","type":"string"},{"internalType":"string","name":"_Address","type":"string"},{"internalType":"string","name":"_City","type":"string"},{"internalType":"string","name":"_State","type":"string"},{"internalType":"uint256","name":"_Zip","type":"uint256"},{"internalType":"uint256","name":"_SID","type":"uint256"},{"internalType":"bool","name":"_FOB","type":"bool"},{"internalType":"uint256","name":"_userId","type":"uint256"},{"internalType":"address","name":"_userAddress","type":"address"}],"name":"setShipFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"},{"internalType":"string","name":"_Name","type":"string"},{"internalType":"string","name":"_Address","type":"string"},{"internalType":"string","name":"_City","type":"string"},{"internalType":"string","name":"_State","type":"string"},{"internalType":"uint256","name":"_Zip","type":"uint256"},{"internalType":"uint256","name":"_Location","type":"uint256"},{"internalType":"bool","name":"_FOB","type":"bool"},{"internalType":"uint256","name":"_userId","type":"uint256"},{"internalType":"address","name":"_userAddress","type":"address"}],"name":"setShipTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"},{"internalType":"uint256","name":"_shipmentAgencyId","type":"uint256"},{"internalType":"address","name":"_shipmentAgencyAddress","type":"address"}],"name":"setShipmentAgency","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"},{"internalType":"string","name":"_Name","type":"string"},{"internalType":"string","name":"_Address","type":"string"},{"internalType":"string","name":"_City","type":"string"},{"internalType":"string","name":"_State","type":"string"},{"internalType":"uint256","name":"_Zip","type":"uint256"},{"internalType":"uint256","name":"_AppointmentNo","type":"uint256"},{"internalType":"string","name":"_Date","type":"string"},{"internalType":"string","name":"_DeliveryInstruction","type":"string"}],"name":"setThirdPartyDetails","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"shipmentID","type":"string"},{"internalType":"string","name":"_date","type":"string"},{"internalType":"string","name":"_time","type":"string"},{"internalType":"string","name":"_longitude","type":"string"},{"internalType":"string","name":"_latitude","type":"string"},{"internalType":"string","name":"_reporterCompanyName","type":"string"},{"internalType":"bool","name":"_approved","type":"bool"},{"internalType":"string","name":"_remarks","type":"string"}],"name":"setTrackingData","outputs":[],"stateMutability":"nonpayable","type":"function"}]'