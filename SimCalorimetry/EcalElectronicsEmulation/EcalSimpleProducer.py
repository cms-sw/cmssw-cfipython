import FWCore.ParameterSet.Config as cms

def EcalSimpleProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalSimpleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
