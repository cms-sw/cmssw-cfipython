import FWCore.ParameterSet.Config as cms

def TauGenJetProducer(**kwargs):
  mod = cms.EDProducer('TauGenJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
