import FWCore.ParameterSet.Config as cms

def TestESDummyDataAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestESDummyDataAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
