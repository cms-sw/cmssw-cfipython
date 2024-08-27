import FWCore.ParameterSet.Config as cms

def FakeGctInputTester(**kwargs):
  mod = cms.EDAnalyzer('FakeGctInputTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
