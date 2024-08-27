import FWCore.ParameterSet.Config as cms

def EtMinPFJetSelector(**kwargs):
  mod = cms.EDFilter('EtMinPFJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
