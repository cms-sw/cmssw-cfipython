import FWCore.ParameterSet.Config as cms

def PixelVertexSoAFromCUDA(*args, **kwargs):
  mod = cms.EDProducer('PixelVertexSoAFromCUDA',
    src = cms.InputTag('pixelVerticesCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
