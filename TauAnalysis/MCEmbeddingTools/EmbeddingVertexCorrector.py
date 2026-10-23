import FWCore.ParameterSet.Config as cms

def EmbeddingVertexCorrector(*args, **kwargs):
  mod = cms.EDProducer('EmbeddingVertexCorrector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
