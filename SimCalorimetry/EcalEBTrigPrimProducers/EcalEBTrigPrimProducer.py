import FWCore.ParameterSet.Config as cms

def EcalEBTrigPrimProducer(**kwargs):
  mod = cms.EDProducer('EcalEBTrigPrimProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
