import FWCore.ParameterSet.Config as cms

def EcalZeroSuppressionProducer(**kwargs):
  mod = cms.EDProducer('EcalZeroSuppressionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
