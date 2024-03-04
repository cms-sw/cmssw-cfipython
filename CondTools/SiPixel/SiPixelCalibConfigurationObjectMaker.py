import FWCore.ParameterSet.Config as cms

def SiPixelCalibConfigurationObjectMaker(**kwargs):
  mod = cms.EDAnalyzer('SiPixelCalibConfigurationObjectMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
