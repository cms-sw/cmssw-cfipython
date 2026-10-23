import FWCore.ParameterSet.Config as cms

def FakeTTrig(*args, **kwargs):
  mod = cms.EDAnalyzer('FakeTTrig',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
