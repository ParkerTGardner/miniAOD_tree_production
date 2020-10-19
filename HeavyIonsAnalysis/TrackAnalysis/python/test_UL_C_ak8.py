import FWCore.ParameterSet.Config as cms
import HLTrigger.HLTfilters.hltHighLevel_cfi
process = cms.Process('Analysis')

# input files
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames = cms.untracked.vstring(
        "root://cms-xrd-global.cern.ch///store//data/Run2018C/JetHT/MINIAOD/12Nov2019_UL2018_rsb-v1/10000/015CDDF7-DBCB-094D-861E-54F73012741A.root"
        ),
    )

# number of events to process, set to -1 to process all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

# load Global Tag, geometry, etc.
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

# root output
process.TFileService = cms.Service("TFileService",
    fileName = cms.string("output_UL_C_ak8.root"))

process.hlt = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hlt.HLTPaths = ['HLT_AK8PFJet500*'] # for allphysics
process.hlt.andOr = cms.bool(True)
process.hlt.throw = cms.bool(False)
process.eventFilterHLT = cms.Sequence(process.hlt)


process.analyzer = cms.EDAnalyzer('TrackAnalyzer',
    doTrack = cms.untracked.bool(True),
    trackPtMin = cms.untracked.double(0.01),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
    packedCandSrc = cms.InputTag("packedPFCandidates"),
    lostTracksSrc = cms.InputTag("lostTracks"),
    beamSpotSrc = cms.untracked.InputTag('offlineBeamSpot'),
    jets2 = cms.InputTag("slimmedJetsAK8")
)

# main forest sequence
process.runAnalyzer = cms.Path(
    process.eventFilterHLT*
    process.analyzer
    )

