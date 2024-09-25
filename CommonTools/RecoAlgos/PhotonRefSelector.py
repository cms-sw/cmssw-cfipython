import FWCore.ParameterSet.Config as cms

def PhotonRefSelector(*args, **kwargs):
  mod = cms.EDFilter('PhotonRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
