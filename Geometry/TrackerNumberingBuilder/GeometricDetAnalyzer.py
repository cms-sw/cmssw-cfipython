import FWCore.ParameterSet.Config as cms

def GeometricDetAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('GeometricDetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
