import FWCore.ParameterSet.Config as cms

def L1CaloInputScalesGenerator(**kwargs):
  mod = cms.EDAnalyzer('L1CaloInputScalesGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
