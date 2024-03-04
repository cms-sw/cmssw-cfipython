import FWCore.ParameterSet.Config as cms

def ExistingDictionaryTestProducer(**kwargs):
  mod = cms.EDProducer('ExistingDictionaryTestProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
