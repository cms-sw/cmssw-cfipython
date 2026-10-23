import FWCore.ParameterSet.Config as cms

def PixelVertexProducerClusters(*args, **kwargs):
  mod = cms.EDProducer('PixelVertexProducerClusters',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
