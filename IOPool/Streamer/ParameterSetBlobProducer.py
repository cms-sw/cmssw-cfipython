import FWCore.ParameterSet.Config as cms

def ParameterSetBlobProducer(**kwargs):
  mod = cms.EDProducer('ParameterSetBlobProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
