import FWCore.ParameterSet.Config as cms

hltEventNumberFilter = cms.EDFilter('HLTEventNumberFilter',
  period = cms.int32(4096),
  invert = cms.bool(True)
)
