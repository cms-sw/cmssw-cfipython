import FWCore.ParameterSet.Config as cms

def HcalGeometryPlan1Tester(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalGeometryPlan1Tester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
