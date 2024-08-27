import FWCore.ParameterSet.Config as cms

def EcalHaloDataProducer(**kwargs):
  mod = cms.EDProducer('EcalHaloDataProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
