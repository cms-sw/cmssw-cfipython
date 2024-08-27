import FWCore.ParameterSet.Config as cms

def SiPixelGainCalibrationAnalysis(**kwargs):
  mod = cms.EDAnalyzer('SiPixelGainCalibrationAnalysis',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
