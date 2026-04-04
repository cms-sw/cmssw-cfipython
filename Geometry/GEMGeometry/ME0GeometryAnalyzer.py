import FWCore.ParameterSet.Config as cms

def ME0GeometryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ME0GeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
