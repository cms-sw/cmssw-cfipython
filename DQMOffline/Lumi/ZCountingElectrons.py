import FWCore.ParameterSet.Config as cms

def ZCountingElectrons(*args, **kwargs):
  mod = cms.EDProducer('ZCountingElectrons',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
