import FWCore.ParameterSet.Config as cms

def PhotonCoreProducer(**kwargs):
  mod = cms.EDProducer('PhotonCoreProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
