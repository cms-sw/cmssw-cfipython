import FWCore.ParameterSet.Config as cms

def PFTester(*args, **kwargs):
  mod = cms.EDAnalyzer('PFTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
