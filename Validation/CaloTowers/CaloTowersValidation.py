import FWCore.ParameterSet.Config as cms

def CaloTowersValidation(*args, **kwargs):
  mod = cms.EDProducer('CaloTowersValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
