import FWCore.ParameterSet.Config as cms

def CPEAccessTester(**kwargs):
  mod = cms.EDAnalyzer('CPEAccessTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
