import FWCore.ParameterSet.Config as cms

def SiPixelCalibConfigurationReadDb(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelCalibConfigurationReadDb',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
