import FWCore.ParameterSet.Config as cms

def edmtest_one_SharedResourcesAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::one::SharedResourcesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
