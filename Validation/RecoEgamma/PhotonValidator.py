import FWCore.ParameterSet.Config as cms

def PhotonValidator(**kwargs):
  mod = cms.EDProducer('PhotonValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
