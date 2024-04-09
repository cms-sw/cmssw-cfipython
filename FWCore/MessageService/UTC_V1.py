import FWCore.ParameterSet.Config as cms

def UTC_V1(**kwargs):
  mod = cms.EDAnalyzer('UTC_V1',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod