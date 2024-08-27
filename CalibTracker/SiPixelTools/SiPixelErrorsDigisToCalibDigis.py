import FWCore.ParameterSet.Config as cms

def SiPixelErrorsDigisToCalibDigis(**kwargs):
  mod = cms.EDAnalyzer('SiPixelErrorsDigisToCalibDigis',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
