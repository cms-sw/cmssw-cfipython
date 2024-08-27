import FWCore.ParameterSet.Config as cms

def EcalTPSkimmer(**kwargs):
  mod = cms.EDProducer('EcalTPSkimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
