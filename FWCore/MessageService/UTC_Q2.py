import FWCore.ParameterSet.Config as cms

def UTC_Q2(**kwargs):
  mod = cms.EDAnalyzer('UTC_Q2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
