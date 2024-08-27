import FWCore.ParameterSet.Config as cms

def DeleteEarlyRefProdProducer(**kwargs):
  mod = cms.EDProducer('DeleteEarlyRefProdProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
