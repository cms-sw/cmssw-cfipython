import FWCore.ParameterSet.Config as cms

ecalBarrelCellParameterDump = cms.EDAnalyzer('ecalBarrelCellParameterDump',
  SubDetector = cms.int32(1),
  mightGet = cms.optional.untracked.vstring
)
