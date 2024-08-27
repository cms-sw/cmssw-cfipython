import FWCore.ParameterSet.Config as cms

def MixCollectionValidation(**kwargs):
  mod = cms.EDProducer('MixCollectionValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
