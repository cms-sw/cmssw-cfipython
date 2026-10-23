import FWCore.ParameterSet.Config as cms

def DTGeometryTest(*args, **kwargs):
  mod = cms.EDAnalyzer('DTGeometryTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
