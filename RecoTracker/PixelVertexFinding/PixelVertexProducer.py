import FWCore.ParameterSet.Config as cms

def PixelVertexProducer(**kwargs):
  mod = cms.EDProducer('PixelVertexProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
