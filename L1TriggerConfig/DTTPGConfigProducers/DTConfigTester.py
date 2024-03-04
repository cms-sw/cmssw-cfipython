import FWCore.ParameterSet.Config as cms

def DTConfigTester(**kwargs):
  mod = cms.EDAnalyzer('DTConfigTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
