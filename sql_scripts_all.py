create_table_linelist = ('CREATE TABLE IF NOT EXISTS linelist (`IP` varchar(500) DEFAULT NULL, \
  `State` varchar(500) DEFAULT NULL, \
  `SurgeCommand` varchar(500) DEFAULT NULL, \
  `LGA` varchar(500) DEFAULT NULL, \
  `FacilityName` varchar(500) DEFAULT NULL, \
  `Pepid_datim` varchar(500) PRIMARY KEY, \
  `patient_id` double DEFAULT NULL, \
  `Pepid` varchar(500) NOT NULL, \
  `HospitalNo` varchar(500) DEFAULT NULL, \
  `Sex` varchar(500) DEFAULT NULL, \
`KP_Type` varchar(500) DEFAULT NULL, \
  `Date_Enrolled` timestamp(6) NULL DEFAULT NULL, \
  `AgeAtStartofART` double DEFAULT NULL, \
  `AgeAtStart_InMonth` double DEFAULT NULL, \
`CurrentAge` double DEFAULT NULL, \
  `ARTStartDate` timestamp(6) NULL DEFAULT NULL, \
  `LastPickupDate` timestamp(6) NULL DEFAULT NULL, \
`NextAppmt` timestamp(6) NULL DEFAULT NULL, \
  `DaysOfARVRefill` double DEFAULT NULL, \
  `RegLineAtStart` varchar(500) DEFAULT NULL, \
  `ARTRegAtStart` varchar(500) DEFAULT NULL, \
  `CurrentRegLine` varchar(500) DEFAULT NULL, \
  `CurrentARTReg` varchar(500) DEFAULT NULL, \
  `PregStatus` varchar(500) DEFAULT NULL, \
  `CurrentVL` double DEFAULT NULL, \
  `DateOfCurrentVL` timestamp(6) NULL DEFAULT NULL, \
  `ViralLoadIndication` varchar(500) DEFAULT NULL, \
  `Date_Result_Received` timestamp(6) NULL DEFAULT NULL, \
  `Last_VL_Sample_Date` timestamp(6) NULL DEFAULT NULL, \
  `Initial_CD4_Date` timestamp(6) NULL DEFAULT NULL, \
  `initial_CD4` double DEFAULT NULL, \
  `Last_CD4_Date` timestamp(6) NULL DEFAULT NULL, \
  `Last_CD4` double DEFAULT NULL, \
  `CurrentARTStatus_28Days` varchar(500) DEFAULT NULL, \
  `DaysInterval` double DEFAULT NULL, \
  `TI` varchar(500) DEFAULT NULL, \
  `DOB` date DEFAULT NULL, \
  `Surname` varchar(500) DEFAULT NULL, \
  `FirstName` varchar(500) DEFAULT NULL, \
  `Phone_No` varchar(500) DEFAULT NULL, \
  `Address` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL, \
  `Pill_Balance` double DEFAULT NULL, \
  `Next_Pickup_Date` timestamp(6) NULL DEFAULT NULL, \
  `DATIMCode` varchar(500) DEFAULT NULL, \
  `MonthOnART` double DEFAULT NULL, \
  `Last_Weight` double DEFAULT NULL, \
  `Last_Weight_Date` timestamp(6) NULL DEFAULT NULL, \
  `Biometrics_Captured` timestamp(6) NULL DEFAULT NULL, \
  `Recapture_Count` double DEFAULT NULL, \
  `Date_Last_Recaptured` timestamp(6) NULL DEFAULT NULL, \
  `Eligible_For_IPT` varchar(500) DEFAULT NULL, \
  `Date_IPT_start` timestamp(6) NULL DEFAULT NULL, \
  `Outcome_of_IPT` varchar(500) DEFAULT NULL, \
  `Date_of_Outcome` timestamp(6) NULL DEFAULT NULL, \
  `Last_Clinic_Visit_Date` timestamp(6) NULL DEFAULT NULL, \
  `Systolic_BP` double DEFAULT NULL, \
  `Diastolic_BP` double DEFAULT NULL, \
  `Next_Clinical_Appt_Date` timestamp(6) NULL DEFAULT NULL, \
  `Last_TB_Screening_Date` timestamp(6) NULL DEFAULT NULL, \
  `Last_TB_Screening_Status` varchar(500) DEFAULT NULL, \
  `TB_Investigations` varchar(500) DEFAULT NULL, \
  `Investig_Result` varchar(500) DEFAULT NULL, \
  `Date_TB_Investig` timestamp(6) NULL DEFAULT NULL, \
  `Reason_for_Tracking` varchar(500) DEFAULT NULL, \
  `Tracking_Date` timestamp(6) NULL DEFAULT NULL, \
  `Reason_for_Defaulting1` varchar(500) DEFAULT NULL, \
  `Reason_for_Termination` varchar(500) DEFAULT NULL, \
  `Date_of_Termination` timestamp(6) NULL DEFAULT NULL, \
`Facility_Transferred_To` varchar(500) DEFAULT NULL, \
  `Last_EAC_Session_Date` timestamp(6) NULL DEFAULT NULL, \
  `EAC_Session_Type` varchar(500) DEFAULT NULL, \
  `EAC_ARV_Plan` varchar(500) DEFAULT NULL, \
  `Date_VL_Before_EAC` timestamp(6) NULL DEFAULT NULL, \
  `VL_Before_EAC` double DEFAULT NULL, \
  `Date_VL_After_EAC` timestamp(6) NULL DEFAULT NULL, \
  `VL_After_EAC` double DEFAULT NULL, \
  `List_Parameters` varchar(500) DEFAULT NULL, \
  `Date_List_Gen` timestamp(6) NULL DEFAULT NULL)')

create_ahd_linelist = ("CREATE TABLE IF NOT EXISTS `ahd_linelist` ( \
  `IP` varchar(500) DEFAULT NULL,\
  `State` varchar(500) DEFAULT NULL,\
  `SurgeCommand` varchar(500) DEFAULT NULL,\
  `LGA` varchar(500) DEFAULT NULL,\
  `FacilityName` varchar(500) DEFAULT NULL,\
  `Pepid_datim` varchar(500) PRIMARY KEY,\
  `Pepid` varchar(500) NOT NULL,\
  `person_id` double DEFAULT NULL,\
  `Sex` varchar(500) NOT NULL,\
  `Date_Enrolled` timestamp(6) NULL DEFAULT NULL,\
  `ARTStartDate` timestamp(6) NULL DEFAULT NULL,\
  `Sample_Collection_Date` timestamp(6) NULL DEFAULT NULL,\
  `Indication_for_AHD` varchar(500) DEFAULT NULL,\
  `CD4_LFA_Result` varchar(500) DEFAULT NULL,\
  `TB_LF_LAM_Result` varchar(500) DEFAULT NULL,\
  `Date_TB_LF_LAM_Result_Received` timestamp(6) NULL DEFAULT NULL,\
  `Serology_For_CrAg_Result` varchar(500) DEFAULT NULL,\
  `Date_Serology_For_CrAg_Result_Received` timestamp(6) NULL DEFAULT NULL,\
  `CSF_For_CrAg_Result` varchar(500) DEFAULT NULL,\
  `Date_CSF_For_CrAg_Result_Received` varchar(500) DEFAULT NULL,\
  `ICE_WHO_Staging` varchar(500) DEFAULT NULL)")

create_eid_linelist = ("CREATE TABLE IF NOT EXISTS `eid_linelist` (\
`IP` varchar(500) DEFAULT NULL,\
  `State` varchar(500) DEFAULT NULL,\
  `SurgeCommand` varchar(500) DEFAULT NULL,\
  `LGA` varchar(500) DEFAULT NULL,\
  `FacilityName` varchar(500) DEFAULT NULL,\
  `HEI_Number_datim` varchar(500) PRIMARY KEY,\
  `HEI_Number` varchar(500) NOT NULL,\
  `ChildRegistrationDate` varchar(500) DEFAULT NULL,\
  `Surname` varchar(500) DEFAULT NULL,\
  `FirstName` varchar(500) DEFAULT NULL,\
  `DOB` date DEFAULT NULL,\
  `Sex` varchar(500) DEFAULT NULL,\
  `CurrentAge` double DEFAULT NULL,\
  `PhoneNumber` varchar(500) DEFAULT NULL,\
  `WeightAtBirth` varchar(500) DEFAULT NULL,\
  `lengthAtBirth` varchar(500) DEFAULT NULL,\
  `HeadCircumferenceAtBirth` varchar(500) DEFAULT NULL,\
  `ChildMUACAtBirth` varchar(500) DEFAULT NULL,\
  `APGAR_ScoreAtBirth` varchar(500) DEFAULT NULL,\
  `ChildGivenHepatitisB_Immunoglobulin` varchar(500) DEFAULT NULL,\
  `HighRiskHIVExposedInfant` varchar(500) DEFAULT NULL,\
  `ARVProphylaxis` varchar(500) DEFAULT NULL,\
  `TimingOfARVProphylaxis` varchar(500) DEFAULT NULL,\
  `ImmunizationReceivedAtBirth` varchar(500) DEFAULT NULL,\
  `FollowUpDate` varchar(500) DEFAULT NULL,\
  `TimingOfMotherARTInitiation` varchar(500) DEFAULT NULL,\
  `WeightAtFollowUP` varchar(500) DEFAULT NULL,\
  `lengthAtFollowUp` varchar(500) DEFAULT NULL,\
  `HeadCircumferenceAtFollowUp` varchar(500) DEFAULT NULL,\
  `MID_UpperARM_CircumferenceAtFollowUp` varchar(500) DEFAULT NULL,\
  `ChildMUACAtFollowUp` varchar(500) DEFAULT NULL,\
  `BMI_MUACAtFollowUp` varchar(500) DEFAULT NULL,\
  `CTX_GivenToChild` varchar(500) DEFAULT NULL,\
  `InfantFeedingMethod` varchar(500) DEFAULT NULL,\
  `PCR_Type` varchar(500) DEFAULT NULL,\
  `SampleCollectionDate` timestamp(6) NULL DEFAULT NULL,\
  `DateSampleSent` timestamp(6) NULL DEFAULT NULL,\
  `DateResultReceivedAtFacility` timestamp(6) NULL DEFAULT NULL,\
  `DateCaregiverWasGivenPCRResult` timestamp(6) NULL DEFAULT NULL,\
  `PCR_Result` varchar(500) DEFAULT NULL,\
  `RapidTestType` varchar(500) DEFAULT NULL,\
  `RapidTestDate` varchar(500) DEFAULT NULL,\
  `RapidTestResult` varchar(500) DEFAULT NULL,\
  `Outcome_At_18Month` varchar(500) DEFAULT NULL,\
  `ARTStartDate_IfPositive` varchar(500) DEFAULT NULL)")

create_hts_linelist = ("CREATE TABLE IF NOT EXISTS `hts_linelist` (\
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `City` varchar(255) DEFAULT NULL,\
  `Datim_Code` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `Datim_HTS_ClientCode` varchar(255) PRIMARY KEY,\
  `patient_id` double DEFAULT NULL,\
  `HTS_ClientCode` varchar(255) NOT NULL,\
  `PEPFAR_Number_IfOnART` varchar(255) DEFAULT NULL,\
  `birthdate` date DEFAULT NULL,\
  `Sex` varchar(255) DEFAULT NULL,\
  `CurrentAge` double DEFAULT NULL,\
  `given_name` varchar(255) DEFAULT NULL,\
  `family_name` varchar(255) DEFAULT NULL,\
  `PhoneNumber` varchar(255) DEFAULT NULL,\
  `VisitDate` varchar(255) DEFAULT NULL,\
  `Test_VisitDate_Validation` varchar(255) DEFAULT NULL,\
  `KindOfHTS` varchar(255) DEFAULT NULL,\
  `setting` varchar(255) DEFAULT NULL,\
  `FirstTimeVisit` varchar(255) DEFAULT NULL,\
  `TypeOfSession` varchar(255) DEFAULT NULL,\
  `ReferredFrom` varchar(255) DEFAULT NULL,\
  `MaritalStatus` varchar(255) DEFAULT NULL,\
  `FromIndex` varchar(255) DEFAULT NULL,\
  `IndexClientID_Validation` varchar(255) DEFAULT NULL,\
  `IndexClientID` varchar(255) DEFAULT NULL,\
  `IndexType` varchar(255) DEFAULT NULL,\
  `IndexClientName` varchar(255) DEFAULT NULL,\
  `HIVScreeningTest` varchar(255) DEFAULT NULL,\
  `HIVScreeningTestDate` date DEFAULT NULL,\
  `HIVConfirmatoryTest` varchar(255) DEFAULT NULL,\
  `HIVConfirmatoryTestDate` date DEFAULT NULL,\
  `HIV_FinalResult` varchar(255) DEFAULT NULL,\
  `Opt_Out_of_RTRI?` varchar(255) DEFAULT NULL,\
  `Opt_Out_of_RTRI_Validation` varchar(255) DEFAULT NULL,\
  `HIVRecencyTestName` varchar(255) DEFAULT NULL,\
  `VerifyRecencyNumber` varchar(255) DEFAULT NULL,\
  `ControlLine` varchar(255) DEFAULT NULL,\
  `VerificationLine` varchar(255) DEFAULT NULL,\
  `LongTermLine` varchar(255) DEFAULT NULL,\
  `HIVRecencyTestDate` date DEFAULT NULL,\
  `RecencyInterpretation` varchar(255) DEFAULT NULL,\
  `ViralLoadRequest` varchar(255) DEFAULT NULL,\
  `VLSampleCollectionDate` varchar(255) DEFAULT NULL,\
  `PCR_LabNo` varchar(255) DEFAULT NULL,\
  `SampleType` varchar(255) DEFAULT NULL,\
  `PCR_Laboratory` varchar(255) DEFAULT NULL,\
  `HIV_ViralLoad` varchar(255) DEFAULT NULL,\
  `FinalHIVRecencyResult` varchar(255) DEFAULT NULL,\
  `NoOfPatnerElicited` varchar(255) DEFAULT NULL,\
  `PartnerFullName_1` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_1` varchar(255) DEFAULT NULL,\
  `IndexType_Partner1` varchar(255) DEFAULT NULL,\
  `PartnerFullName_2` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_2` varchar(255) DEFAULT NULL,\
  `IndexType_Partner2` varchar(255) DEFAULT NULL,\
  `PartnerFullName_3` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_3` varchar(255) DEFAULT NULL,\
  `IndexType_Partner3` varchar(255) DEFAULT NULL,\
  `PartnerFullName_4` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_4` varchar(255) DEFAULT NULL,\
  `IndexType_Partner4` varchar(255) DEFAULT NULL,\
  `PartnerFullName_5` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_5` varchar(255) DEFAULT NULL,\
  `IndexType_Partner5` varchar(255) DEFAULT NULL,\
  `PartnerFullName_6` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_6` varchar(255) DEFAULT NULL,\
  `IndexType_Partner6` varchar(255) DEFAULT NULL)")

create_lims_emr_linelist = ("CREATE TABLE IF NOT EXISTS `lims_emr_daily_report` (\
  `IP` varchar(500) DEFAULT NULL,\
  `State` varchar(500) DEFAULT NULL,\
  `SurgeCommand` varchar(500) DEFAULT NULL,\
  `LGA` varchar(500) DEFAULT NULL,\
  `FacilityName` varchar(500) DEFAULT NULL,\
  `Manifest_id` varchar(500) DEFAULT NULL,\
  `Sample_Collected_Date` varchar(500) DEFAULT NULL,\
  `Date_Sample_sent` varchar(500) DEFAULT NULL,\
  `Sample_Status` varchar(500) DEFAULT NULL,\
  `sample_id` varchar(500) DEFAULT NULL,\
  `patient_id` varchar(500) DEFAULT NULL,\
  `PEPID` varchar(500) NOT NULL,\
  `Date_Sample_Receieved_at_PCRlab` varchar(500) DEFAULT NULL,\
  `Assay_Date` varchar(500) DEFAULT NULL,\
  `Date_Result_Dispatched` varchar(500) DEFAULT NULL)")

create_otz_linelist = ("CREATE TABLE IF NOT EXISTS `otz_linelist` (\
  `IP` varchar(500) DEFAULT NULL,\
  `State` varchar(500) DEFAULT NULL,\
  `SurgeCommand` varchar(500) DEFAULT NULL,\
  `LGA` varchar(500) DEFAULT NULL,\
  `FacilityName` varchar(500) DEFAULT NULL,\
  `Pepid_datim` varchar(500) PRIMARY KEY,\
  `patient_id` double DEFAULT NULL,\
  `Pepid` varchar(500) NOT NULL,\
  `Visit_Date` timestamp(6) NULL DEFAULT NULL,\
  `Date_Enrolled_Into_OTZ` varchar(500) DEFAULT NULL,\
  `Full_Disclosure` varchar(500) DEFAULT NULL,\
  `Full_Disclosure_Date` timestamp(6) NULL DEFAULT NULL,\
  `Positive_Living` varchar(500) DEFAULT NULL,\
  `Positive_Living_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Treatment_Literacy` varchar(500) DEFAULT NULL,\
  `Treatment_Literacy_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Enrolled_Into_OTZ_Plus` varchar(500) DEFAULT NULL,\
  `Date_Enrolled_Into_OTZ_Plus` varchar(500) DEFAULT NULL,\
  `Adolescents_Participation` varchar(500) DEFAULT NULL,\
  `Adolescents_Participation_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Leadership_Training` varchar(500) DEFAULT NULL,\
  `Leadership_Training_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Peer_to_Peer_Mentorship` varchar(500) DEFAULT NULL,\
  `Peer_to_Peer_Mentorship_Comp_Date` varchar(500) DEFAULT NULL,\
  `Role_of_OTZ_in_95_95_95` varchar(500) DEFAULT NULL,\
  `Role_of_OTZ_in_95_95_95_Comp_Date` varchar(500) DEFAULT NULL,\
  `Transitioned_to_Adult_Clinic` varchar(500) DEFAULT NULL,\
  `Date_Transitioned_to_Adult_Clinic` varchar(500) DEFAULT NULL,\
  `OTZ_Program_Outcome` varchar(500) DEFAULT NULL)")

create_pmtct_linelist = ("CREATE TABLE IF NOT EXISTS `pmtct_linelist` (\
  `IP` varchar(500) DEFAULT NULL,\
  `State` varchar(500) DEFAULT NULL,\
  `SurgeCommand` varchar(500) DEFAULT NULL,\
  `LGA` varchar(500) DEFAULT NULL,\
  `FacilityName` varchar(500) DEFAULT NULL,\
  `City` varchar(500) DEFAULT NULL,\
  `Datim_Code` varchar(500) DEFAULT NULL,\
  `ANC_Number_datim` varchar(500) PRIMARY KEY,\
  `ANC_Number` varchar(500) NOT NULL,\
  `PEPFAR_Number(IfOnART)` varchar(500) DEFAULT NULL,\
  `person_id` double DEFAULT NULL,\
  `birthdate` date DEFAULT NULL,\
  `Gender` varchar(500) DEFAULT NULL,\
  `CurrentAge` double DEFAULT NULL,\
  `given_name` varchar(500) DEFAULT NULL,\
  `family_name` varchar(500) DEFAULT NULL,\
  `PhoneNumber` varchar(500) DEFAULT NULL,\
  `Address` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,\
  `Client_LGA` varchar(500) DEFAULT NULL,\
  `LGA_Latitude` varchar(500) DEFAULT NULL,\
  `LGA_Longitude` varchar(500) DEFAULT NULL,\
  `GeneralANC_VisitDate` varchar(500) DEFAULT NULL,\
  `LMP_DATE` varchar(500) DEFAULT NULL,\
  `GA` double DEFAULT NULL,\
  `Gravida` double DEFAULT NULL,\
  `Parity` double DEFAULT NULL,\
  `Point_Of_Entry` varchar(500) DEFAULT NULL,\
  `EDD` varchar(500) DEFAULT NULL,\
  `PMTCT_HTS_Date` varchar(500) DEFAULT NULL,\
  `PMTCT_HTS_SettingRegister` varchar(500) DEFAULT NULL,\
  `PMTCT_HTS_Register_Date` varchar(500) DEFAULT NULL,\
  `Previously_Known_HIV_Status` varchar(500) DEFAULT NULL,\
  `Date_Previously_Tested_Positive` varchar(500) DEFAULT NULL,\
  `HIV_TestAccepted` varchar(500) DEFAULT NULL,\
  `HIV_ReTesting` varchar(500) DEFAULT NULL,\
  `ResultOfHIVTest` varchar(500) DEFAULT NULL,\
  `Received_HIV_Test_Result` varchar(500) DEFAULT NULL)")

create_full_pharmacy_complement = ("CREATE TABLE IF NOT EXISTS `full_pharmacy_complement` (\
  `IP` varchar(500) DEFAULT NULL,\
  `State` varchar(500) DEFAULT NULL,\
  `SurgeCommand` varchar(500) DEFAULT NULL,\
  `LGA` varchar(500) DEFAULT NULL,\
  `FacilityName` varchar(500) DEFAULT NULL,\
  `DATIMCode` varchar(500) DEFAULT NULL,\
  `Pepid_datim` varchar(500) PRIMARY KEY,\
  `PEPID` varchar(500) NOT NULL,\
  `patient_id` double DEFAULT NULL,\
  `LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `encounter_id` double DEFAULT NULL,\
  `DaysOfARVRefill` double DEFAULT NULL,\
  `Pill_Balance` varchar(500) DEFAULT NULL,\
  `Next_Pickup_Date` timestamp(6) NULL DEFAULT NULL,\
  `CurrentARTReg` varchar(500) DEFAULT NULL,\
  `CurrentRegLine` varchar(500) DEFAULT NULL,\
  `ARV_Drug_Strength` varchar(500) DEFAULT NULL,\
  `OI_Drug_CTX` varchar(500) DEFAULT NULL,\
  `CTX_Strength` varchar(500) DEFAULT NULL,\
  `OI_Drug_INH` varchar(500) DEFAULT NULL,\
  `INH_Strength` varchar(500) DEFAULT NULL,\
  `DSD_Model` varchar(500) DEFAULT NULL,\
  `DDD_Fac_Disp` varchar(500) DEFAULT NULL,\
  `PregStatus` varchar(500) DEFAULT NULL)")

create_last_5_pharmacy = ("CREATE TABLE IF NOT EXISTS `last_5_pharmacy` (\
  `IP` varchar(500) DEFAULT NULL,\
  `State` varchar(500) DEFAULT NULL,\
  `SurgeCommand` varchar(500) DEFAULT NULL,\
  `LGA` varchar(500) DEFAULT NULL,\
  `FacilityName` varchar(500) DEFAULT NULL,\
  `DatimCode` varchar(500) DEFAULT NULL,\
  `Pepid_Datim` varchar(500) PRIMARY KEY,\
  `patient_id` double DEFAULT NULL,\
  `PEPID` varchar(500) NOT NULL,\
  `1_LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `1_DaysOfARVRefill` double DEFAULT NULL,\
  `1_NextAppmt` timestamp(6) NULL DEFAULT NULL,\
  `2_LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `2_DaysOfARVRefill` double DEFAULT NULL,\
  `2_NextAppmt` timestamp(6) NULL DEFAULT NULL,\
  `3_LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `3_DaysOfARVRefill` double DEFAULT NULL,\
  `3_NextAppmt` timestamp(6) NULL DEFAULT NULL,\
  `4_LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `4_DaysOfARVRefill` double DEFAULT NULL,\
  `4_NextAppmt` timestamp(6) NULL DEFAULT NULL,\
  `5_LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `5_DaysOfARVRefill` double DEFAULT NULL,\
  `5_NextAppmt` timestamp(6) NULL DEFAULT NULL)")

create_mobile_hts_tracker = ("CREATE TABLE IF NOT EXISTS `mobile_hts_tracker` (\
    `IP` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `State` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `SurgeCommand` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `LGA` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `patient_Id` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `pep_id` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `facility_name` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `datim_code` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `patient_date_created` DATETIME DEFAULT NULL,\
    `baseline_date` DATETIME DEFAULT NULL,\
    `recapture_date` DATETIME DEFAULT NULL,\
    `encounter_date` DATETIME DEFAULT NULL,\
    `encounter_date_created` DATETIME DEFAULT NULL,\
    `current_status_90days` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `latitude` double DEFAULT NULL,\
    `longitude` double DEFAULT NULL,\
    `entry_source` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `baseline_source` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `recapture_source` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL)")


create_ncd_linelist = ("CREATE TABLE IF NOT EXISTS `ncd_linelist` (\
  `IP` varchar(500) DEFAULT NULL,\
  `State` varchar(500) DEFAULT NULL,\
  `SurgeCommand` varchar(500) DEFAULT NULL,\
  `LGA` varchar(500) DEFAULT NULL,\
  `FacilityName` varchar(500) DEFAULT NULL,\
  `PATIENT ID` double DEFAULT NULL,\
  `PATIENT IDENTIFIER` varchar(500) DEFAULT NULL,\
  `GENDER` varchar(500) DEFAULT NULL,\
  `PHONE NUMBER` varchar(500) DEFAULT NULL,\
  `PATIENT NAME` varchar(500) DEFAULT NULL,\
  `FAMILY NAME` varchar(500) DEFAULT NULL,\
  `AGE` double DEFAULT NULL,\
  `ADDRESS` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,\
  `STATE_Res` varchar(500) DEFAULT NULL,\
  `LGA_Res` varchar(500) DEFAULT NULL,\
  `SITE` varchar(500) DEFAULT NULL,\
  `SERVICE AREA NAME` varchar(500) DEFAULT NULL,\
  `RISK ASSESSMENT SCORE` double DEFAULT NULL,\
  `HYPERTENSIVE` varchar(500) DEFAULT NULL,\
  `MEDICATION FOR HTN` varchar(500) DEFAULT NULL,\
  `LATEST BP UPPER` double DEFAULT NULL,\
  `LATEST BP LOWER` double DEFAULT NULL,\
  `DIABETIC` varchar(500) DEFAULT NULL,\
  `MEDICATION FOR DM` varchar(500) DEFAULT NULL,\
  `LATEST RBS` double DEFAULT NULL,\
  `BMI WEIGHT` double DEFAULT NULL,\
  `BMI HEIGHT` double DEFAULT NULL,\
  `BMI` double DEFAULT NULL,\
  `BMI RANGE` varchar(500) DEFAULT NULL,\
  `NCD SCREENING SCORE` double DEFAULT NULL,\
  `HIV STATUS` varchar(500) DEFAULT NULL,\
  `ART STATUS` varchar(500) DEFAULT NULL,\
  `HIV OUTCOME` varchar(500) DEFAULT NULL,\
  `NCD OUTCOME` varchar(500) DEFAULT NULL,\
  `ENCOUNTER DATE` timestamp(6) NULL DEFAULT NULL,\
  `DATE CREATED` timestamp(6) NULL DEFAULT NULL)")


create_pbs_linelist = ("CREATE TABLE IF NOT EXISTS `pbs_linelist` (\
  `IP` varchar(500) DEFAULT NULL,\
  `State` varchar(500) DEFAULT NULL,\
  `SurgeCommand` varchar(500) DEFAULT NULL,\
  `LGA` varchar(500) DEFAULT NULL,\
  `FacilityName` varchar(500) DEFAULT NULL,\
  `DATIM_Code` varchar(500) DEFAULT NULL,\
  `Pepid_datim` varchar(500) PRIMARY KEY,\
  `patient_Id` double DEFAULT NULL,\
  `PEPID` varchar(500) NOT NULL,\
  `Initial_Date_Captured` timestamp(6) NULL DEFAULT NULL,\
  `No_Initial_Finger_Captured` double DEFAULT NULL,\
  `Date_Recapture` timestamp(6) NULL DEFAULT NULL,\
  `No_Recaptured_Finger` double DEFAULT NULL,\
  `Recapture_Count` double DEFAULT NULL,\
  `Last_Visit_Date` timestamp(6) NULL DEFAULT NULL,\
  `Last_Encounter` varchar(500) DEFAULT NULL,\
  `Total_%_PBS_Quality` double DEFAULT NULL,\
  `L_Thumb_Quality(%)` double DEFAULT NULL,\
  `L_Index_Quality(%)` double DEFAULT NULL,\
  `L_Middle_Quality(%)` double DEFAULT NULL,\
  `L_Wedding_Quality(%)` double DEFAULT NULL,\
  `L_Small_Quality(%)` double DEFAULT NULL,\
  `R_Thumb_Quality(%)` double DEFAULT NULL,\
  `R_Index_Quality(%)` double DEFAULT NULL,\
  `R_Middle_Quality(%)` double DEFAULT NULL,\
  `R_Wedding_Quality(%)` double DEFAULT NULL,\
  `R_Small_Quality(%)` double DEFAULT NULL,\
  `Initial_LeftThumb` double DEFAULT NULL, \
  `Initial_LeftIndex` double DEFAULT NULL,\
  `Initial_LeftMiddle` double DEFAULT NULL,\
  `Initial_LeftWedding` double DEFAULT NULL,\
  `Initial_LeftSmall` double DEFAULT NULL,\
  `Initial_RightThumb` double DEFAULT NULL,\
  `Initial_RightIndex` double DEFAULT NULL,\
  `Initial_RightMiddle` double DEFAULT NULL,\
  `Initial_RightWedding` double DEFAULT NULL,\
  `Initial_RightSmall` double DEFAULT NULL,\
  `LeftThumb` double DEFAULT NULL,\
  `LeftIndex` double DEFAULT NULL,\
  `LeftMiddle` double DEFAULT NULL,\
  `LeftWedding` double DEFAULT NULL,\
  `LeftSmall` double DEFAULT NULL,\
  `RightThumb` double DEFAULT NULL,\
  `RightIndex` double DEFAULT NULL,\
  `RightMiddle` double DEFAULT NULL,\
  `RightWedding` double DEFAULT NULL,\
  `RightSmall` double DEFAULT NULL)")


create_client_tracking_and_discontinuation = ("CREATE TABLE IF NOT EXISTS `client_tracking_and_discontinuation` (\
  `State` VARCHAR(100) CHARACTER SET utf8,\
  `LGA` VARCHAR(100) CHARACTER SET utf8,\
  `Facilty Name` TEXT CHARACTER SET utf8,\
  `DATIM Code` TEXT CHARACTER SET utf8,\
  `Hospital No` VARCHAR(50) CHARACTER SET utf8 DEFAULT '',\
  `Patient ID` VARCHAR(50) CHARACTER SET utf8 DEFAULT '',\
  `Date of Tracking` VARCHAR(72) CHARACTER SET utf8 DEFAULT NULL,\
  `Reason for Tracking` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Date of Last Actual Contact/ Appointment` DATETIME DEFAULT NULL,\
  `Date of Missed Scheduled Appointment` DATETIME DEFAULT NULL,\
  `Client Verification` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Indication for Client Verification` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Patient Care in Facility Discontinued` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Date of Discontinuation` DATETIME DEFAULT NULL,\
  `Reason for Discontinuation` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Facility transferred to` MEDIUMTEXT CHARACTER SET utf8,\
  `Reason for Tracking1` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Cause of Death` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
  `VA Cause of Death` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Adult Causes` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Child Causes` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Other cause of death` MEDIUMTEXT CHARACTER SET utf8,\
  `Reason to Discontinue Care` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Discontinue Care other specify` MEDIUMTEXT CHARACTER SET utf8,\
  `Date of Lost to follow up` DATETIME DEFAULT NULL,\
  `Reason for Lost to follow up` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Reason for Lost to follow up_Other` MEDIUMTEXT CHARACTER SET utf8)")


create_recency_standalone = ("CREATE TABLE IF NOT EXISTS `recency_standalone` (\
    `IP` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `State` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `SurgeCommand` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `LGA` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `City_of_Residence` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `DATIMCode` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `FacilityName` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `patient_id` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Datim_HTS_ClientCode` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `HTS_ClientCode` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `PEPFAR_Number_IfOnART` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Birthdate` DATETIME DEFAULT NULL,\
    `Sex` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Age <= 15 (at Test)?` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `given_name` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `family_name` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `PhoneNumber` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `VisitDate` DATETIME DEFAULT NULL,\
    `Test_VisitDate_Validation` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `KindOfHTS` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Setting` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `HIVScreeningTestDate` DATETIME DEFAULT NULL,\
    `Opt_Out_of_RTRI?` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `HIVRecencyTestName` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Recency Number` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `ControlLine` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `VerificationLine` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `LongTermLine` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `HIVRecencyTestDate` DATETIME DEFAULT NULL,\
    `RecencyInterpretation` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `ViralLoadRequest` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `VLSampleCollectionDate` DATETIME DEFAULT NULL,\
    `PCR_LabNo` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `SampleType` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `PCR_Laboratory` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `HIV_ViralLoad` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `FinalHIVRecencyResult` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL)")

create_Nutritional_Status = ("CREATE TABLE IF NOT EXISTS `Nutritional_Status` (\
    `IP` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `State` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `SurgeCommand` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `LGA` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `FacilityName` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `DATIMCode` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `patient_id` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `PEPID` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Birthdate` DATETIME DEFAULT NULL,\
    `SEX` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Educational level` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Occupation` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Next_of_kin` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `NOK_Phone_no` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `LGA of residence` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `State of Residence` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Date of enrolment into care` DATETIME DEFAULT NULL,\
    `Date of ART initiation` DATETIME DEFAULT NULL,\
    `Q1_Visit_Date(W)` DATETIME DEFAULT NULL,\
    `Q1_Weight(kg)` double DEFAULT NULL,\
    `Q1_Visit_Date(H)` DATETIME DEFAULT NULL,\
    `Q1_Height(cm)` double DEFAULT NULL,\
    `Q1_BMI` double DEFAULT NULL,\
    `Q2_Visit_Date(W)` DATETIME DEFAULT NULL,\
    `Q2_Weight(kg)` double DEFAULT NULL,\
    `Q2_Visit_Date(H)` DATETIME DEFAULT NULL,\
    `Q2_Height(cm)` double DEFAULT NULL,\
    `Q2_BMI` double DEFAULT NULL,\
    `Q3_Visit_Date(W)` DATETIME DEFAULT NULL,\
    `Q3_Weight(kg)` double DEFAULT NULL,\
    `Q3_Visit_Date(H)` double DEFAULT NULL,\
    `Q3_Height(cm)` double DEFAULT NULL,\
    `Q3_BMI` double DEFAULT NULL,\
    `Q4_Visit_Date(W)` DATETIME DEFAULT NULL,\
    `Q4_Weight(kg)` double DEFAULT NULL,\
    `Q4_Visit_Date(H)` DATETIME DEFAULT NULL,\
    `Q4_Height(cm)` double DEFAULT NULL,\
    `Q4_BMI` double DEFAULT NULL,\
    `Marital status` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Surname` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `FirstName` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Phone_No` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL)")




