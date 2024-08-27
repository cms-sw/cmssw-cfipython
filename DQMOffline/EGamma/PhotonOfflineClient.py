import FWCore.ParameterSet.Config as cms

def PhotonOfflineClient(**kwargs):
  mod = cms.EDProducer('PhotonOfflineClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
