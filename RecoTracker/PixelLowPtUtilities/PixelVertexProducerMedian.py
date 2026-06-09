import FWCore.ParameterSet.Config as cms

def PixelVertexProducerMedian(*args, **kwargs):
  mod = cms.EDProducer('PixelVertexProducerMedian',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
