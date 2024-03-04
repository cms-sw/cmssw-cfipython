import FWCore.ParameterSet.Config as cms

def EcalSimpleProducer(**kwargs):
  mod = cms.EDProducer('EcalSimpleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
