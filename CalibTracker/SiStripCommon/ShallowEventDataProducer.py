import FWCore.ParameterSet.Config as cms

def ShallowEventDataProducer(**kwargs):
  mod = cms.EDProducer('ShallowEventDataProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
