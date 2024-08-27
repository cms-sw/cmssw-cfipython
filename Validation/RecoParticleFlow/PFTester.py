import FWCore.ParameterSet.Config as cms

def PFTester(**kwargs):
  mod = cms.EDAnalyzer('PFTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
