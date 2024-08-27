import FWCore.ParameterSet.Config as cms

def L1GtTrigReport(**kwargs):
  mod = cms.EDAnalyzer('L1GtTrigReport',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
