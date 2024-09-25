import FWCore.ParameterSet.Config as cms

def TestFindProduct(*args, **kwargs):
  mod = cms.EDAnalyzer('TestFindProduct',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
