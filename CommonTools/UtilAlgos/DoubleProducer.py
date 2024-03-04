import FWCore.ParameterSet.Config as cms

def DoubleProducer(**kwargs):
  mod = cms.EDProducer('DoubleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
