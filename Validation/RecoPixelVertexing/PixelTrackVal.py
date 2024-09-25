import FWCore.ParameterSet.Config as cms

def PixelTrackVal(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelTrackVal',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
