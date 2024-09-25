import FWCore.ParameterSet.Config as cms

def SiPixelSCurveCalibrationAnalysis(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelSCurveCalibrationAnalysis',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
