import FWCore.ParameterSet.Config as cms

def MissingDictionaryTestProducer(*args, **kwargs):
  mod = cms.EDProducer('MissingDictionaryTestProducer',
    inputTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
