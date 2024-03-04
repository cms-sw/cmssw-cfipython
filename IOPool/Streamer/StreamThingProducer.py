import FWCore.ParameterSet.Config as cms

def StreamThingProducer(**kwargs):
  mod = cms.EDProducer('StreamThingProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
