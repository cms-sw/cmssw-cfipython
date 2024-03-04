import FWCore.ParameterSet.Config as cms

def MinPatMETProducer(**kwargs):
  mod = cms.EDProducer('MinPatMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
