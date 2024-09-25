import FWCore.ParameterSet.Config as cms

def PixelDigisTest(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelDigisTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
