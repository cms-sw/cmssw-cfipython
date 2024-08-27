import FWCore.ParameterSet.Config as cms

def UTC_SUMMARY(**kwargs):
  mod = cms.EDAnalyzer('UTC_SUMMARY',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
