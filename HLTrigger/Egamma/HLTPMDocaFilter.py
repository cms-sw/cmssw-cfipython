import FWCore.ParameterSet.Config as cms

def HLTPMDocaFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTPMDocaFilter',
    saveTags = cms.bool(True),
    candTag = cms.InputTag('HltZeePMMassFilter'),
    docaDiffPerpCutHigh = cms.double(0.055691),
    docaDiffPerpCutLow = cms.double(0),
    nZcandcut = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
