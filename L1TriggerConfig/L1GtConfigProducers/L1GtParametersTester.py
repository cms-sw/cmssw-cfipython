import FWCore.ParameterSet.Config as cms

def L1GtParametersTester(**kwargs):
  mod = cms.EDAnalyzer('L1GtParametersTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
