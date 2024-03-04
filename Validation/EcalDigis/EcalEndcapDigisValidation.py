import FWCore.ParameterSet.Config as cms

def EcalEndcapDigisValidation(**kwargs):
  mod = cms.EDProducer('EcalEndcapDigisValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
