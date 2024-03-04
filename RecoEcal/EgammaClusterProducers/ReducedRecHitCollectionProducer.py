import FWCore.ParameterSet.Config as cms

def ReducedRecHitCollectionProducer(**kwargs):
  mod = cms.EDProducer('ReducedRecHitCollectionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
