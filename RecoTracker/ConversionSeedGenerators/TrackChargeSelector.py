import FWCore.ParameterSet.Config as cms

def TrackChargeSelector(*args, **kwargs):
  mod = cms.EDFilter('TrackChargeSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
