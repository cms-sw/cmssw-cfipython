import FWCore.ParameterSet.Config as cms

def EcalZeroSuppressionProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalZeroSuppressionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
