import FWCore.ParameterSet.Config as cms

def HcalGeometryPlan1Tester(**kwargs):
  mod = cms.EDAnalyzer('HcalGeometryPlan1Tester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
