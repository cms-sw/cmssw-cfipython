import FWCore.ParameterSet.Config as cms

def PixelVertexVal(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelVertexVal',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
