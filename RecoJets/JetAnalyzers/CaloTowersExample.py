import FWCore.ParameterSet.Config as cms

def CaloTowersExample(**kwargs):
  mod = cms.EDAnalyzer('CaloTowersExample',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
