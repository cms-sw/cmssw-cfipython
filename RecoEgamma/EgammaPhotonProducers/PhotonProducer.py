import FWCore.ParameterSet.Config as cms

def PhotonProducer(**kwargs):
  mod = cms.EDProducer('PhotonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
