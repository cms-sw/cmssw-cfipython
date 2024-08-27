import FWCore.ParameterSet.Config as cms

def EcalCompactTrigPrimProducer(**kwargs):
  mod = cms.EDProducer('EcalCompactTrigPrimProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
