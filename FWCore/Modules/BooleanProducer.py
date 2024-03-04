import FWCore.ParameterSet.Config as cms

def BooleanProducer(**kwargs):
  mod = cms.EDProducer('BooleanProducer',
    value = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
