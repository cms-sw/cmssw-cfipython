import FWCore.ParameterSet.Config as cms

def CaloCellGeometryTester(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloCellGeometryTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
