import FWCore.ParameterSet.Config as cms

def EcalCondDBWriter(*args, **kwargs):
  mod = cms.EDProducer('EcalCondDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
