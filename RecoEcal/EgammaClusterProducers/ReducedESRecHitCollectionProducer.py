import FWCore.ParameterSet.Config as cms

def ReducedESRecHitCollectionProducer(**kwargs):
  mod = cms.EDProducer('ReducedESRecHitCollectionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
