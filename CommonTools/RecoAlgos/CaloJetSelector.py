import FWCore.ParameterSet.Config as cms

def CaloJetSelector(**kwargs):
  mod = cms.EDFilter('CaloJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
