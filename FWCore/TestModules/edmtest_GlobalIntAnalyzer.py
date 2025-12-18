import FWCore.ParameterSet.Config as cms

def edmtest_GlobalIntAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::GlobalIntAnalyzer',
    source = cms.required.InputTag,
    expected = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
