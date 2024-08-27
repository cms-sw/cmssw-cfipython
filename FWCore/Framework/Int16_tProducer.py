import FWCore.ParameterSet.Config as cms

def Int16_tProducer(**kwargs):
  mod = cms.EDProducer('Int16_tProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
