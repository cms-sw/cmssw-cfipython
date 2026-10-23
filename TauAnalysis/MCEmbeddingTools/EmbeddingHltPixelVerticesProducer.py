import FWCore.ParameterSet.Config as cms

def EmbeddingHltPixelVerticesProducer(*args, **kwargs):
  mod = cms.EDProducer('EmbeddingHltPixelVerticesProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
