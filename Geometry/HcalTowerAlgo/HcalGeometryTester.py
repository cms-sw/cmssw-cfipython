import FWCore.ParameterSet.Config as cms

def HcalGeometryTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalGeometryTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
