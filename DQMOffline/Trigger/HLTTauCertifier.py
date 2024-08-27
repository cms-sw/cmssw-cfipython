import FWCore.ParameterSet.Config as cms

def HLTTauCertifier(**kwargs):
  mod = cms.EDProducer('HLTTauCertifier',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
