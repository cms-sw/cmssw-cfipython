import FWCore.ParameterSet.Config as cms

def TrackSelectorForValidation(**kwargs):
  mod = cms.EDFilter('TrackSelectorForValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
