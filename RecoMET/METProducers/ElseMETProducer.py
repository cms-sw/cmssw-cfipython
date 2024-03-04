import FWCore.ParameterSet.Config as cms

def ElseMETProducer(**kwargs):
  mod = cms.EDProducer('ElseMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
