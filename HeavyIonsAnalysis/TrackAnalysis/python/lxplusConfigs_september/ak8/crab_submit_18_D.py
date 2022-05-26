from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferOutputs = True

config.section_('JobType')
config.JobType.psetName = 'pset_18_D.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['output_UL_2018_D_ak8_400.root']
config.JobType.allowUndistributedCMSSW = True
#config.JobType.maxMemoryMB = 4000
#config.JobType.inputFiles = ['HeavyIonRPVRcd_PbPb2018_offline.db']
config.section_('Data')
config.Data.inputDataset = '/JetHT/Run2018D-12Nov2019_UL2018_rsb-v1/MINIAOD'
#used to be '/JetHT/Run2018D-12Nov2019_UL2018-v4/MINIAOD'

config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader'

config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'

config.Data.splitting = 'Automatic'
#config.Data.unitsPerJob = 'Automatic'
config.Data.publication = False

#config.Data.outLFNDirBase = '/store/user/pgardner/MINIAOD_2018_UL_D_ak8_new'

config.Data.outLFNDirBase = '/store/group/phys_heavyions/flowcorr/miniAOD_out_HLT_PF400ak8/MINIAOD_2018_UL_D_ak8_new/'

#config.Data.totalUnits        = 1500 #for test only

config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T3_US_Rice'
