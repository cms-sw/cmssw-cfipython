import FWCore.ParameterSet.Config as cms

def TrackingFailureFilter(**kwargs):
  mod = cms.EDFilter('TrackingFailureFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
