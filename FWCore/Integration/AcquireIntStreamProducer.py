import FWCore.ParameterSet.Config as cms

def AcquireIntStreamProducer(**kwargs):
  mod = cms.EDProducer('AcquireIntStreamProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
