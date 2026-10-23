import FWCore.ParameterSet.Config as cms

def EcalCompactTrigPrimProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalCompactTrigPrimProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
