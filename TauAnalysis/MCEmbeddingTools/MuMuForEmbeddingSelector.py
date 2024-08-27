import FWCore.ParameterSet.Config as cms

def MuMuForEmbeddingSelector(**kwargs):
  mod = cms.EDProducer('MuMuForEmbeddingSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
