import FWCore.ParameterSet.Config as cms

def TestSuite(*args, **kwargs):
  mod = cms.EDAnalyzer('TestSuite',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
