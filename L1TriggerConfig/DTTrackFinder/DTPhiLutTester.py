import FWCore.ParameterSet.Config as cms

def DTPhiLutTester(**kwargs):
  mod = cms.EDAnalyzer('DTPhiLutTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
