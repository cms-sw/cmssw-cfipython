import FWCore.ParameterSet.Config as cms

def VIDUsageExample(*args, **kwargs):
  mod = cms.EDAnalyzer('VIDUsageExample',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
