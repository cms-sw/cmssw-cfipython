import FWCore.ParameterSet.Config as cms

def SiPixelGainCalibrationAnalysis(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelGainCalibrationAnalysis',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
