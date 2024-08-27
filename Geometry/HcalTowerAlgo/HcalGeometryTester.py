import FWCore.ParameterSet.Config as cms

def HcalGeometryTester(**kwargs):
  mod = cms.EDAnalyzer('HcalGeometryTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
