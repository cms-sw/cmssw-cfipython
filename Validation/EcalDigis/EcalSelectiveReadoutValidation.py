import FWCore.ParameterSet.Config as cms

def EcalSelectiveReadoutValidation(**kwargs):
  mod = cms.EDProducer('EcalSelectiveReadoutValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
