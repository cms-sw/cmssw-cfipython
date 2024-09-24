import FWCore.ParameterSet.Config as cms

def IsoPhotonEBSelectorAndSkim(*args, **kwargs):
  mod = cms.EDFilter('IsoPhotonEBSelectorAndSkim',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
