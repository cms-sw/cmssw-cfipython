import FWCore.ParameterSet.Config as cms

def GenHIEventProducer(**kwargs):
  mod = cms.EDProducer('GenHIEventProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
