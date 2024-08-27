import FWCore.ParameterSet.Config as cms

def EcalCondDBWriter(**kwargs):
  mod = cms.EDProducer('EcalCondDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
