import FWCore.ParameterSet.Config as cms

def TrackChargeSelector(**kwargs):
  mod = cms.EDFilter('TrackChargeSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
