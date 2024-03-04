import FWCore.ParameterSet.Config as cms

def L1CaloJetProducer(**kwargs):
  mod = cms.EDProducer('L1CaloJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
