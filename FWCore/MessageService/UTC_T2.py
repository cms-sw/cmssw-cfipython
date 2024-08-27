import FWCore.ParameterSet.Config as cms

def UTC_T2(**kwargs):
  mod = cms.EDAnalyzer('UTC_T2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
