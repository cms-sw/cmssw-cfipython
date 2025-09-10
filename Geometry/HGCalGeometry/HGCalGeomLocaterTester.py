import FWCore.ParameterSet.Config as cms

def HGCalGeomLocaterTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalGeomLocaterTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
