import FWCore.ParameterSet.Config as cms

def HLTCountNumberOfTrack(*args, **kwargs):
  mod = cms.EDFilter('HLTCountNumberOfTrack',
    saveTags = cms.bool(True),
    src = cms.InputTag(''),
    MinN = cms.int32(0),
    MaxN = cms.int32(99999),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
