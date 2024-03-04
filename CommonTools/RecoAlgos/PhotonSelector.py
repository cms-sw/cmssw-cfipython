import FWCore.ParameterSet.Config as cms

def PhotonSelector(**kwargs):
  mod = cms.EDFilter('PhotonSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
