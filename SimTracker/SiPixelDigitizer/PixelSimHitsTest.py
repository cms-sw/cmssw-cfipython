import FWCore.ParameterSet.Config as cms

def PixelSimHitsTest(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelSimHitsTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
