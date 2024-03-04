import FWCore.ParameterSet.Config as cms

def WriteCTPPSPixelAnalysisMask(**kwargs):
  mod = cms.EDAnalyzer('WriteCTPPSPixelAnalysisMask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
