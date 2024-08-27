import FWCore.ParameterSet.Config as cms

def SiPixelCalibConfigurationReadDb(**kwargs):
  mod = cms.EDAnalyzer('SiPixelCalibConfigurationReadDb',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
