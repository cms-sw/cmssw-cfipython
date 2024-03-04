import FWCore.ParameterSet.Config as cms

def HFNoseGeometryTester(**kwargs):
  mod = cms.EDAnalyzer('HFNoseGeometryTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
