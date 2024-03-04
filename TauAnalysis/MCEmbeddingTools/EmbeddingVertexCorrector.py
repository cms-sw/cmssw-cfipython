import FWCore.ParameterSet.Config as cms

def EmbeddingVertexCorrector(**kwargs):
  mod = cms.EDProducer('EmbeddingVertexCorrector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
