import FWCore.ParameterSet.Config as cms

def PixelVertexProducer(*args, **kwargs):
  mod = cms.EDProducer('PixelVertexProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
