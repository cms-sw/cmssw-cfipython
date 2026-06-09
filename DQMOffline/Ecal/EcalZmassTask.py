import FWCore.ParameterSet.Config as cms

def EcalZmassTask(*args, **kwargs):
  mod = cms.EDProducer('EcalZmassTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
