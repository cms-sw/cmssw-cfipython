import FWCore.ParameterSet.Config as cms

def EcalZmassClient(**kwargs):
  mod = cms.EDProducer('EcalZmassClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
