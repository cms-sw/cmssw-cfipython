import FWCore.ParameterSet.Config as cms

def edmtest_TestGetByLabelIntAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('edmtest::TestGetByLabelIntAnalyzer',
    src = cms.required.untracked.InputTag,
    getExceptionCategory = cms.untracked.string(''),
    accessExceptionCategory = cms.untracked.string(''),
    consumes = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
