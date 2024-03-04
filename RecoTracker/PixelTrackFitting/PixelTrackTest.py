import FWCore.ParameterSet.Config as cms

def PixelTrackTest(**kwargs):
  mod = cms.EDAnalyzer('PixelTrackTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
