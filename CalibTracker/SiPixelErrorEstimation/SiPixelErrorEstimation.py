import FWCore.ParameterSet.Config as cms

def SiPixelErrorEstimation(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelErrorEstimation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
