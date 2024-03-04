import FWCore.ParameterSet.Config as cms

def GeometryTester(**kwargs):
  mod = cms.EDAnalyzer('GeometryTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
