import FWCore.ParameterSet.Config as cms

def DeleteEarlyRefProdProducer(*args, **kwargs):
  mod = cms.EDProducer('DeleteEarlyRefProdProducer',
    get = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
