import FWCore.ParameterSet.Config as cms

def TPStubValueMapProducer(**kwargs):
  mod = cms.EDProducer('TPStubValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
