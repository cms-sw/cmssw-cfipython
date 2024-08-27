import FWCore.ParameterSet.Config as cms

def PhotonColMerger(**kwargs):
  mod = cms.EDProducer('PhotonColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
