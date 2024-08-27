import FWCore.ParameterSet.Config as cms

def BrilClient(**kwargs):
  mod = cms.EDProducer('BrilClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
