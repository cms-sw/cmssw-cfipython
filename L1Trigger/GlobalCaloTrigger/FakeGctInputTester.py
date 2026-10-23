import FWCore.ParameterSet.Config as cms

def FakeGctInputTester(*args, **kwargs):
  mod = cms.EDAnalyzer('FakeGctInputTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
