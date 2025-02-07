import FWCore.ParameterSet.Config as cms

def GaussianZBeamSpotFilter(*args, **kwargs):
  mod = cms.EDFilter('GaussianZBeamSpotFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
