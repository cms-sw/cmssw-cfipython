import FWCore.ParameterSet.Config as cms

def DTGeometryDump(*args, **kwargs):
  mod = cms.EDAnalyzer('DTGeometryDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
