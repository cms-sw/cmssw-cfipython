import FWCore.ParameterSet.Config as cms

def VIDUsageExample(**kwargs):
  mod = cms.EDAnalyzer('VIDUsageExample',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
