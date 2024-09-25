import FWCore.ParameterSet.Config as cms

def SiPixelVCalDB(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelVCalDB',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
