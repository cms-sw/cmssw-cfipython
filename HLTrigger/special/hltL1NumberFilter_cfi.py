import FWCore.ParameterSet.Config as cms

hltL1NumberFilter = cms.EDFilter('HLTL1NumberFilter',
  rawInput = cms.InputTag('source'),
  period = cms.uint32(4096),
  invert = cms.bool(True),
  fedId = cms.int32(812),
  useTCDSEventNumber = cms.bool(False)
)
