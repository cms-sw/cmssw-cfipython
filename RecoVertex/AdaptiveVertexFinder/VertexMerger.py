import FWCore.ParameterSet.Config as cms

def VertexMerger(**kwargs):
  mod = cms.EDProducer('VertexMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
