import FWCore.ParameterSet.Config as cms

def AcquireIntProducer(**kwargs):
  mod = cms.EDProducer('AcquireIntProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
