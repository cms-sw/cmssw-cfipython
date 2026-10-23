import FWCore.ParameterSet.Config as cms

def HGCalGeometryCornerTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalGeometryCornerTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
