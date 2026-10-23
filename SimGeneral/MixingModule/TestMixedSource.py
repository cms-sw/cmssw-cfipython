import FWCore.ParameterSet.Config as cms

def TestMixedSource(*args, **kwargs):
  mod = cms.EDAnalyzer('TestMixedSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
