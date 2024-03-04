import FWCore.ParameterSet.Config as cms

def PixelTrackVal(**kwargs):
  mod = cms.EDAnalyzer('PixelTrackVal',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
