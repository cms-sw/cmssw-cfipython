import FWCore.ParameterSet.Config as cms

def edmtest_GlobalVectorAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::GlobalVectorAnalyzer',
    source = cms.required.InputTag,
    expected = cms.vdouble(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
