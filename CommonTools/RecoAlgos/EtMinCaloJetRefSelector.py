import FWCore.ParameterSet.Config as cms

def EtMinCaloJetRefSelector(**kwargs):
  mod = cms.EDFilter('EtMinCaloJetRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod