import FWCore.ParameterSet.Config as cms

def PixelTrackTest(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelTrackTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
