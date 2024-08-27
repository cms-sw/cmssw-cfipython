import FWCore.ParameterSet.Config as cms

def L1CaloJetHTTProducer(**kwargs):
  mod = cms.EDProducer('L1CaloJetHTTProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
