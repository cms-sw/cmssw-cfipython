import FWCore.ParameterSet.Config as cms

def edmtest_TestGetByLabelThingAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::TestGetByLabelThingAnalyzer',
    src = cms.required.untracked.InputTag,
    getExceptionCategory = cms.untracked.string(''),
    accessExceptionCategory = cms.untracked.string(''),
    consumes = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
