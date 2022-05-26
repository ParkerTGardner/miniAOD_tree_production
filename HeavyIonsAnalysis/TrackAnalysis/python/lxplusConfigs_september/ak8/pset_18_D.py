import FWCore.ParameterSet.Config as cms
import HLTrigger.HLTfilters.hltHighLevel_cfi
process = cms.Process('Analysis')

# input files
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames = cms.untracked.vstring(
        "file:/eos/cms/store/group/phys_heavyions/flowcorr/JetHT/Ak8Jet500Skim_JetHT_Run2018D/210629_021937/0000/ppRun2UL_MINIAOD_2.root"
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
    fileName = cms.string("output_UL_2018_D_ak8_400.root"))

process.hlt = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hlt.HLTPaths = ['HLT_AK8PFJet400_v*'] # for allphysics
process.hlt.andOr = cms.bool(True)
process.hlt.throw = cms.bool(False)
process.eventFilterHLT = cms.Sequence(process.hlt)


process.analyzer = cms.EDAnalyzer('TrackAnalyzer',
    doTrack = cms.untracked.bool(False),
    trackPtMin = cms.untracked.double(0.01),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
    packedCandSrc = cms.InputTag("packedPFCandidates"),
    lostTracksSrc = cms.InputTag("lostTracks"),
    beamSpotSrc = cms.untracked.InputTag('offlineBeamSpot'),
    #jets2 = cms.InputTag("slimmedJets")
    #jets2 = cms.InputTag('slimmedJetsPuppi')
    jets2 = cms.InputTag('slimmedJetsAK8')
    #jets2 = cms.InputTag("slimmedJetsAK8PFPuppiSoftDropPacked")
)

# main forest sequence
process.runAnalyzer = cms.Path(
    process.eventFilterHLT*
    process.analyzer
    )

