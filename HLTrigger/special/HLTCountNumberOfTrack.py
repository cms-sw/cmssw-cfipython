import FWCore.ParameterSet.Config as cms

def HLTCountNumberOfTrack(**kwargs):
  mod = cms.EDFilter('HLTCountNumberOfTrack',
    saveTags = cms.bool(True),
    src = cms.InputTag(''),
    MinN = cms.int32(0),
    MaxN = cms.int32(99999),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
