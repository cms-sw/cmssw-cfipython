import FWCore.ParameterSet.Config as cms

def MissingDictionaryTestProducer(**kwargs):
  mod = cms.EDProducer('MissingDictionaryTestProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
