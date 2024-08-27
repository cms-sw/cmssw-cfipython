import FWCore.ParameterSet.Config as cms

def L1TSummary(**kwargs):
  mod = cms.EDAnalyzer('L1TSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
