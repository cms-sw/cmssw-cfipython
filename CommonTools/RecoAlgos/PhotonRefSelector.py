import FWCore.ParameterSet.Config as cms

def PhotonRefSelector(**kwargs):
  mod = cms.EDFilter('PhotonRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
