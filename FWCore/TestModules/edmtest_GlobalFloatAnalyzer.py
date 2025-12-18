import FWCore.ParameterSet.Config as cms

def edmtest_GlobalFloatAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::GlobalFloatAnalyzer',
    source = cms.required.InputTag,
    expected = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
