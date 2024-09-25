import FWCore.ParameterSet.Config as cms

def WriteCTPPSPixelAnalysisMask(*args, **kwargs):
  mod = cms.EDAnalyzer('WriteCTPPSPixelAnalysisMask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
