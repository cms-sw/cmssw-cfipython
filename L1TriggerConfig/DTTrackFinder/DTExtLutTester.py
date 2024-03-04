import FWCore.ParameterSet.Config as cms

def DTExtLutTester(**kwargs):
  mod = cms.EDAnalyzer('DTExtLutTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
