import FWCore.ParameterSet.Config as cms

def CaloMETProducer(**kwargs):
  mod = cms.EDProducer('CaloMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
