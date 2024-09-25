import FWCore.ParameterSet.Config as cms

def SiPixelErrorsDigisToCalibDigis(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelErrorsDigisToCalibDigis',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
