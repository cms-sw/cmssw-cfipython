import FWCore.ParameterSet.Config as cms

def PixelVertexVal(**kwargs):
  mod = cms.EDAnalyzer('PixelVertexVal',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
