import FWCore.ParameterSet.Config as cms

def EcalPreshowerDigisValidation(*args, **kwargs):
  mod = cms.EDProducer('EcalPreshowerDigisValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
