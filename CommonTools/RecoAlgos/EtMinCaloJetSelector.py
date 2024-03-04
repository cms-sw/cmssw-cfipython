import FWCore.ParameterSet.Config as cms

def EtMinCaloJetSelector(**kwargs):
  mod = cms.EDFilter('EtMinCaloJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
