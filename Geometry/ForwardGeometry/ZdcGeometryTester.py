import FWCore.ParameterSet.Config as cms

def ZdcGeometryTester(*args, **kwargs):
  mod = cms.EDAnalyzer('ZdcGeometryTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
