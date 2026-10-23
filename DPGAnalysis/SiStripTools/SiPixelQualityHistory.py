import FWCore.ParameterSet.Config as cms

def SiPixelQualityHistory(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelQualityHistory',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
