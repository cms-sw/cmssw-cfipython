import FWCore.ParameterSet.Config as cms

def PixelVertexProducerClusters(**kwargs):
  mod = cms.EDProducer('PixelVertexProducerClusters',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
