isComponentType('interfaceview::FV::console','PUBLIC','PI_trigger','SUBPROGRAM','NIL','').
isComponentImplementation('interfaceview::FV::console','PUBLIC','PI_trigger','others','SUBPROGRAM','NIL','others','').
isFeature('ACCESS','interfaceview::IV','console','PI_trigger','PROVIDES','SUBPROGRAM','interfaceview::FV::console::PI_trigger.others','NIL','NIL','').
isProperty('NIL','=>','interfaceview::FV::console','PI_trigger','NIL','NIL','Taste::Associated_Queue_Size','1','').
isProperty('NIL','=>','interfaceview::IV','console','NIL','PI_trigger','Taste::coordinates','"105196 49566"','').
isProperty('NIL','=>','interfaceview::IV','console','NIL','PI_trigger','Taste::RCMoperationKind','cyclic','').
isProperty('NIL','=>','interfaceview::IV','console','NIL','PI_trigger','Taste::RCMperiod','2000 ms','').
isProperty('NIL','=>','interfaceview::IV','console','NIL','PI_trigger','Taste::Deadline','0 ms','').
isProperty('NIL','=>','interfaceview::IV','console','NIL','PI_trigger','Taste::InterfaceName','"trigger"','').
isProperty('NIL','=>','interfaceview::FV::console','PI_trigger','others','NIL','Compute_Execution_Time','0 ms .. 0 ms','').
isSubcomponent('interfaceview::IV','console','others','trigger_impl','SUBPROGRAM','interfaceview::FV::console::PI_trigger.others','NIL','NIL','').
isConnection('SUBPROGRAM ACCESS','interfaceview::IV','console','others','OpToPICnx_trigger_impl','trigger_impl','->','PI_trigger','NIL','').
isConnection('SUBPROGRAM ACCESS','interfaceview::IV','interfaceview','others','console_PI_tm_roberTO_RI_tm','console.PI_tm','->','roberTO.RI_tm','NIL','').
isProperty('NIL','=>','interfaceview::IV','interfaceview','others','console_PI_tm_roberTO_RI_tm','Taste::coordinates','"155554 74836 141003 74836 141003 74864 126452 74864"','').
isComponentType('interfaceview::FV::console','PUBLIC','PI_tm','SUBPROGRAM','NIL','').
isComponentImplementation('interfaceview::FV::console','PUBLIC','PI_tm','others','SUBPROGRAM','NIL','others','').
isFeature('ACCESS','interfaceview::IV','console','PI_tm','PROVIDES','SUBPROGRAM','interfaceview::FV::console::PI_tm.others','NIL','NIL','').
isProperty('NIL','=>','interfaceview::FV::console','PI_tm','NIL','NIL','Taste::Associated_Queue_Size','1','').
isProperty('NIL','=>','interfaceview::IV','console','NIL','PI_tm','Taste::coordinates','"126452 74864"','').
isProperty('NIL','=>','interfaceview::IV','console','NIL','PI_tm','Taste::RCMoperationKind','sporadic','').
isProperty('NIL','=>','interfaceview::IV','console','NIL','PI_tm','Taste::RCMperiod','0 ms','').
isProperty('NIL','=>','interfaceview::IV','console','NIL','PI_tm','Taste::Deadline','0 ms','').
isProperty('NIL','=>','interfaceview::IV','console','NIL','PI_tm','Taste::InterfaceName','"tm"','').
isFeature('PARAMETER','interfaceview::FV::console','PI_tm','packet','IN','NIL','DataView::PusPacket','NIL','NIL','').
isProperty('NIL','=>','interfaceview::FV::console','PI_tm','NIL','packet','Taste::encoding','NATIVE','').
isProperty('NIL','=>','interfaceview::FV::console','PI_tm','others','NIL','Compute_Execution_Time','0 ms .. 0 ms','').
isSubcomponent('interfaceview::IV','console','others','tm_impl','SUBPROGRAM','interfaceview::FV::console::PI_tm.others','NIL','NIL','').
isConnection('SUBPROGRAM ACCESS','interfaceview::IV','console','others','OpToPICnx_tm_impl','tm_impl','->','PI_tm','NIL','').
isConnection('SUBPROGRAM ACCESS','interfaceview::IV','interfaceview','others','roberTO_PI_tc_console_RI_tc','roberTO.PI_tc','->','console.RI_tc','NIL','').
isProperty('NIL','=>','interfaceview::IV','interfaceview','others','roberTO_PI_tc_console_RI_tc','Taste::coordinates','"126452 61242 141003 61242 141003 61214 155554 61214"','').
isComponentType('interfaceview::FV::console','PUBLIC','RI_tc','SUBPROGRAM','NIL','').
isComponentImplementation('interfaceview::FV::console','PUBLIC','RI_tc','others','SUBPROGRAM','NIL','others','').
isImportDeclaration('interfaceview::IV','PUBLIC','interfaceview::FV::roberTO','').
isFeature('ACCESS','interfaceview::IV','console','RI_tc','REQUIRES','SUBPROGRAM','interfaceview::FV::roberTO::PI_tc.others','NIL','NIL','').
isProperty('NIL','=>','interfaceview::IV','console','NIL','RI_tc','Taste::coordinates','"126452 61242"','').
isProperty('NIL','=>','interfaceview::IV','console','NIL','RI_tc','Taste::RCMoperationKind','sporadic','').
isProperty('NIL','=>','interfaceview::IV','console','NIL','RI_tc','Taste::InterfaceName','"tc"','').
isProperty('NIL','=>','interfaceview::IV','console','NIL','RI_tc','Taste::labelInheritance','"true"','').
isFeature('PARAMETER','interfaceview::FV::console','RI_tc','packet','IN','NIL','DataView::PusPacket','NIL','NIL','').
isProperty('NIL','=>','interfaceview::FV::console','RI_tc','NIL','packet','Taste::encoding','NATIVE','').
isPackage('interfaceview::FV::console','PUBLIC','').
isComponentType('interfaceview::IV','PUBLIC','console','SYSTEM','NIL','').
isComponentImplementation('interfaceview::IV','PUBLIC','console','others','SYSTEM','NIL','others','').
isProperty('NIL','=>','interfaceview::IV','console','NIL','NIL','Source_Language','(C)','').
isProperty('NIL','=>','interfaceview::IV','console','NIL','NIL','Taste::Active_Interfaces','any','').
isProperty('NIL','=>','interfaceview::IV','interfaceview','others','console','Taste::coordinates','"86296 49566 126452 82479"','').
isSubcomponent('interfaceview::IV','interfaceview','others','console','SYSTEM','interfaceview::IV::console.others','NIL','NIL','').
isImportDeclaration('interfaceview::IV','PUBLIC','interfaceview::FV::console','').
isImportDeclaration('interfaceview::IV','PUBLIC','Taste','').
isImportDeclaration('interfaceview::FV::console','PUBLIC','Taste','').
isImportDeclaration('interfaceview::IV','PUBLIC','DataView','').
isImportDeclaration('interfaceview::FV::console','PUBLIC','DataView','').
isImportDeclaration('interfaceview::FV::console','PUBLIC','TASTE_IV_Properties','').
isImportDeclaration('interfaceview::IV','PUBLIC','TASTE_IV_Properties','').
isComponentType('interfaceview::FV::roberTO','PUBLIC','PI_tc','SUBPROGRAM','NIL','').
isComponentImplementation('interfaceview::FV::roberTO','PUBLIC','PI_tc','others','SUBPROGRAM','NIL','others','').
isFeature('ACCESS','interfaceview::IV','roberTO','PI_tc','PROVIDES','SUBPROGRAM','interfaceview::FV::roberTO::PI_tc.others','NIL','NIL','').
isProperty('NIL','=>','interfaceview::FV::roberTO','PI_tc','NIL','NIL','Taste::Associated_Queue_Size','1','').
isProperty('NIL','=>','interfaceview::IV','roberTO','NIL','PI_tc','Taste::coordinates','"155554 61214"','').
isProperty('NIL','=>','interfaceview::IV','roberTO','NIL','PI_tc','Taste::RCMoperationKind','sporadic','').
isProperty('NIL','=>','interfaceview::IV','roberTO','NIL','PI_tc','Taste::RCMperiod','0 ms','').
isProperty('NIL','=>','interfaceview::IV','roberTO','NIL','PI_tc','Taste::Deadline','0 ms','').
isProperty('NIL','=>','interfaceview::IV','roberTO','NIL','PI_tc','Taste::InterfaceName','"tc"','').
isFeature('PARAMETER','interfaceview::FV::roberTO','PI_tc','packet','IN','NIL','DataView::PusPacket','NIL','NIL','').
isProperty('NIL','=>','interfaceview::FV::roberTO','PI_tc','NIL','packet','Taste::encoding','NATIVE','').
isProperty('NIL','=>','interfaceview::FV::roberTO','PI_tc','others','NIL','Compute_Execution_Time','0 ms .. 0 ms','').
isSubcomponent('interfaceview::IV','roberTO','others','tc_impl','SUBPROGRAM','interfaceview::FV::roberTO::PI_tc.others','NIL','NIL','').
isConnection('SUBPROGRAM ACCESS','interfaceview::IV','roberTO','others','OpToPICnx_tc_impl','tc_impl','->','PI_tc','NIL','').
isComponentType('interfaceview::FV::roberTO','PUBLIC','PI_trigger','SUBPROGRAM','NIL','').
isComponentImplementation('interfaceview::FV::roberTO','PUBLIC','PI_trigger','others','SUBPROGRAM','NIL','others','').
isFeature('ACCESS','interfaceview::IV','roberTO','PI_trigger','PROVIDES','SUBPROGRAM','interfaceview::FV::roberTO::PI_trigger.others','NIL','NIL','').
isProperty('NIL','=>','interfaceview::FV::roberTO','PI_trigger','NIL','NIL','Taste::Associated_Queue_Size','1','').
isProperty('NIL','=>','interfaceview::IV','roberTO','NIL','PI_trigger','Taste::coordinates','"192528 53430"','').
isProperty('NIL','=>','interfaceview::IV','roberTO','NIL','PI_trigger','Taste::RCMoperationKind','cyclic','').
isProperty('NIL','=>','interfaceview::IV','roberTO','NIL','PI_trigger','Taste::RCMperiod','5000 ms','').
isProperty('NIL','=>','interfaceview::IV','roberTO','NIL','PI_trigger','Taste::Deadline','0 ms','').
isProperty('NIL','=>','interfaceview::IV','roberTO','NIL','PI_trigger','Taste::InterfaceName','"trigger"','').
isProperty('NIL','=>','interfaceview::FV::roberTO','PI_trigger','others','NIL','Compute_Execution_Time','0 ms .. 0 ms','').
isSubcomponent('interfaceview::IV','roberTO','others','trigger_impl','SUBPROGRAM','interfaceview::FV::roberTO::PI_trigger.others','NIL','NIL','').
isConnection('SUBPROGRAM ACCESS','interfaceview::IV','roberTO','others','OpToPICnx_trigger_impl','trigger_impl','->','PI_trigger','NIL','').
isComponentType('interfaceview::FV::roberTO','PUBLIC','RI_tm','SUBPROGRAM','NIL','').
isComponentImplementation('interfaceview::FV::roberTO','PUBLIC','RI_tm','others','SUBPROGRAM','NIL','others','').
isFeature('ACCESS','interfaceview::IV','roberTO','RI_tm','REQUIRES','SUBPROGRAM','interfaceview::FV::console::PI_tm.others','NIL','NIL','').
isProperty('NIL','=>','interfaceview::IV','roberTO','NIL','RI_tm','Taste::coordinates','"155554 74836"','').
isProperty('NIL','=>','interfaceview::IV','roberTO','NIL','RI_tm','Taste::RCMoperationKind','any','').
isProperty('NIL','=>','interfaceview::IV','roberTO','NIL','RI_tm','Taste::InterfaceName','"tm"','').
isProperty('NIL','=>','interfaceview::IV','roberTO','NIL','RI_tm','Taste::labelInheritance','"true"','').
isFeature('PARAMETER','interfaceview::FV::roberTO','RI_tm','packet','IN','NIL','DataView::PusPacket','NIL','NIL','').
isProperty('NIL','=>','interfaceview::FV::roberTO','RI_tm','NIL','packet','Taste::encoding','NATIVE','').
isPackage('interfaceview::FV::roberTO','PUBLIC','').
isComponentType('interfaceview::IV','PUBLIC','roberTO','SYSTEM','NIL','').
isComponentImplementation('interfaceview::IV','PUBLIC','roberTO','others','SYSTEM','NIL','others','').
isProperty('NIL','=>','interfaceview::IV','roberTO','NIL','NIL','Source_Language','(C)','').
isProperty('NIL','=>','interfaceview::IV','roberTO','NIL','NIL','Taste::Active_Interfaces','any','').
isProperty('NIL','=>','interfaceview::IV','interfaceview','others','roberTO','Taste::coordinates','"155554 53430 215877 85537"','').
isSubcomponent('interfaceview::IV','interfaceview','others','roberTO','SYSTEM','interfaceview::IV::roberTO.others','NIL','NIL','').
isImportDeclaration('interfaceview::FV::roberTO','PUBLIC','Taste','').
isImportDeclaration('interfaceview::FV::roberTO','PUBLIC','DataView','').
isImportDeclaration('interfaceview::FV::roberTO','PUBLIC','TASTE_IV_Properties','').
isProperty('_','_','_','_','_','_','LMP::Unparser_ID_Case','AsIs','').
isProperty('_','_','_','_','_','_','LMP::Unparser_Insert_Header','Yes','').
isPackage('interfaceview::IV','PUBLIC','').
isProperty('NIL','=>','interfaceview::IV','NIL','NIL','NIL','Taste::dataView','("DataView")','').
isProperty('NIL','=>','interfaceview::IV','NIL','NIL','NIL','Taste::dataViewPath','("../../esrocos-ws-pus/pus/taste/DataView.aadl")','').
isVersion('AADL2.1','TASTE type interfaceview','','generated code: do not edit').
isProperty('NIL','=>','interfaceview::IV','NIL','NIL','NIL','Taste::coordinates','"0 0 297000 210000"','').
isProperty('NIL','=>','interfaceview::IV','NIL','NIL','NIL','Taste::version','"1.3"','').
isComponentType('interfaceview::IV','PUBLIC','interfaceview','SYSTEM','NIL','').
isComponentImplementation('interfaceview::IV','PUBLIC','interfaceview','others','SYSTEM','NIL','others','').

