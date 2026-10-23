import FWCore.ParameterSet.Config as cms

def GeometryTester(*args, **kwargs):
  mod = cms.EDAnalyzer('GeometryTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
