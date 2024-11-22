import FWCore.ParameterSet.Config as cms

def PhotonSelector(*args, **kwargs):
  mod = cms.EDFilter('PhotonSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
