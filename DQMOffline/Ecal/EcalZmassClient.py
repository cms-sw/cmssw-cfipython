import FWCore.ParameterSet.Config as cms

def EcalZmassClient(*args, **kwargs):
  mod = cms.EDProducer('EcalZmassClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
