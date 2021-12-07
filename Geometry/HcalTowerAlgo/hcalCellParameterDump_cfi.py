import FWCore.ParameterSet.Config as cms

hcalCellParameterDump = cms.EDAnalyzer('HcalCellParameterDump',
  SubDetector = cms.int32(1),
  mightGet = cms.optional.untracked.vstring
)
