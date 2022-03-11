import FWCore.ParameterSet.Config as cms

detStatus = cms.EDFilter('DetStatus',
  DebugOn = cms.untracked.bool(False),
  AndOr = cms.bool(True),
  ApplyFilter = cms.bool(True),
  DetectorType = cms.vstring(),
  mightGet = cms.optional.untracked.vstring
)
