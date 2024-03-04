import FWCore.ParameterSet.Config as cms

def SiPixelSCurveCalibrationAnalysis(**kwargs):
  mod = cms.EDAnalyzer('SiPixelSCurveCalibrationAnalysis',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
