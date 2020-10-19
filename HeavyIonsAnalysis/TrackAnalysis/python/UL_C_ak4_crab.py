from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferOutputs = True

config.section_('JobType')
config.JobType.psetName = 'test_UL_C_ak4.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['output_UL_C_ak4.root']
config.JobType.allowUndistributedCMSSW = True
#config.JobType.maxMemoryMB = 4000
#config.JobType.inputFiles = ['HeavyIonRPVRcd_PbPb2018_offline.db']

config.section_('Data')
config.Data.inputDataset = '/JetHT/Run2018C-12Nov2019_UL2018_rsb-v1/MINIAOD'
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader'



config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'


config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 150
config.Data.publication = False
config.Data.outLFNDirBase = '/store/user/pgardner/MINIAOD_UL_C_ak4'


#config.Data.ignoreLocality = True
#config.Data.totalUnits        = 12000 ###cesar: for test only


#config.Data.outLFNDirBase = '/store/user/abaty/ZAnalysis_Forest_2018_HIHardProbesSkim_SingleEle20_DoubleEle10/'
#config.Data.outLFNDirBase = '/store/group/phys_heavyions/abaty/2015pp_TrackTrigger_Forest_v3'
#config.Data.publishDataName = 'VirginRAW_2010_HICorePhysics_SKIM_Cent_0_5'
#config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader'

config.section_('User')

config.section_('Site')
#config.Site.blacklist = ['T2_US_Florida']
#config.Site.whitelist = ['T2_BE_UCL']
config.Site.storageSite = 'T3_US_Rice'
#config.Site.whitelist         = ['T2_BR_SPRACE','T2_CH_CERN','T2_BE_IIHE','T2_US_*','T1_US_*','T1_FR_*','T2_FR_*','T1_IT_*','T2_IT_*','T3_US_*','T1_DE_*','T1_ES_*','T1_RU_*','T1_UK_*','T2_FI_HIP','T2_RU_*','T2_UK_*','T2_AT_Vienna']
#config.Site.storageSite = 'T2_US_MIT'
