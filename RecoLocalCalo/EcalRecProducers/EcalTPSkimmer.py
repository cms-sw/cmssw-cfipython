import FWCore.ParameterSet.Config as cms

def EcalTPSkimmer(*args, **kwargs):
  mod = cms.EDProducer('EcalTPSkimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
