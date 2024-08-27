import FWCore.ParameterSet.Config as cms

def ZCountingElectrons(**kwargs):
  mod = cms.EDProducer('ZCountingElectrons',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
