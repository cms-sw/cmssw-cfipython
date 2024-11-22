import FWCore.ParameterSet.Config as cms

def DTGeometryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DTGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
