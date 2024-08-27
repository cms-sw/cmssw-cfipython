import FWCore.ParameterSet.Config as cms

def EmbeddingLHEProducer(**kwargs):
  mod = cms.EDProducer('EmbeddingLHEProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
