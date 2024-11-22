import FWCore.ParameterSet.Config as cms

def SiPixelCalibConfigurationObjectMaker(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelCalibConfigurationObjectMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
