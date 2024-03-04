import FWCore.ParameterSet.Config as cms

def IsoPhotonEBSelectorAndSkim(**kwargs):
  mod = cms.EDFilter('IsoPhotonEBSelectorAndSkim',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
