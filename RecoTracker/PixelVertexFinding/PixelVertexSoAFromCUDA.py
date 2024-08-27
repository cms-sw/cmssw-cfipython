import FWCore.ParameterSet.Config as cms

def PixelVertexSoAFromCUDA(**kwargs):
  mod = cms.EDProducer('PixelVertexSoAFromCUDA',
    src = cms.InputTag('pixelVerticesCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
