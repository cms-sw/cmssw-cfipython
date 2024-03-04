import FWCore.ParameterSet.Config as cms

def GenPUProtonProducer(**kwargs):
  mod = cms.EDProducer('GenPUProtonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
