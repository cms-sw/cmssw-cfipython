import FWCore.ParameterSet.Config as cms

def EmbeddingHltPixelVerticesProducer(**kwargs):
  mod = cms.EDProducer('EmbeddingHltPixelVerticesProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
