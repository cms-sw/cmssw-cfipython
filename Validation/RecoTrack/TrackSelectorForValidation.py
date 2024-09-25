import FWCore.ParameterSet.Config as cms

def TrackSelectorForValidation(*args, **kwargs):
  mod = cms.EDFilter('TrackSelectorForValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
