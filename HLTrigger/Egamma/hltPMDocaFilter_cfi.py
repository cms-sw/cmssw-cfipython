import FWCore.ParameterSet.Config as cms

hltPMDocaFilter = cms.EDFilter('HLTPMDocaFilter',
  saveTags = cms.bool(True),
  candTag = cms.InputTag('HltZeePMMassFilter'),
  docaDiffPerpCutHigh = cms.double(0.055691),
  docaDiffPerpCutLow = cms.double(0),
  nZcandcut = cms.int32(1)
)
