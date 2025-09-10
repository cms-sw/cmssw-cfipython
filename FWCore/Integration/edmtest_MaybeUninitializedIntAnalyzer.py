import FWCore.ParameterSet.Config as cms

def edmtest_MaybeUninitializedIntAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::MaybeUninitializedIntAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
