import FWCore.ParameterSet.Config as cms

def GeometricTimingDetAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('GeometricTimingDetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
