import FWCore.ParameterSet.Config as cms

def ME0GeometryDump(*args, **kwargs):
  mod = cms.EDAnalyzer('ME0GeometryDump',
    verbose = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
