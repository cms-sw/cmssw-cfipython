import FWCore.ParameterSet.Config as cms

def edmtest_GlobalStringAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::GlobalStringAnalyzer',
    source = cms.required.InputTag,
    expected = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
