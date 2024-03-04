import FWCore.ParameterSet.Config as cms

def BasicGenTester(**kwargs):
  mod = cms.EDAnalyzer('BasicGenTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
