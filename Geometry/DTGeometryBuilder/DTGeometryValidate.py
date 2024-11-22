import FWCore.ParameterSet.Config as cms

def DTGeometryValidate(*args, **kwargs):
  mod = cms.EDAnalyzer('DTGeometryValidate',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
