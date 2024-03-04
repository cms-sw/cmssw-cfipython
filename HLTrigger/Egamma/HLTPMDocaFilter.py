import FWCore.ParameterSet.Config as cms

def HLTPMDocaFilter(**kwargs):
  mod = cms.EDFilter('HLTPMDocaFilter',
    saveTags = cms.bool(True),
    candTag = cms.InputTag('HltZeePMMassFilter'),
    docaDiffPerpCutHigh = cms.double(0.055691),
    docaDiffPerpCutLow = cms.double(0),
    nZcandcut = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
