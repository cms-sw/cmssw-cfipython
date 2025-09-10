import FWCore.ParameterSet.Config as cms

def edmtest_PrintProcessInformation(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::PrintProcessInformation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
