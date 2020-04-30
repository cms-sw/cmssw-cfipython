import FWCore.ParameterSet.Config as cms

ecalEndcapCellParameterDump = cms.EDAnalyzer('ecalEndcapCellParameterDump',
  SubDetector = cms.int32(1),
  mightGet = cms.optional.untracked.vstring
)
