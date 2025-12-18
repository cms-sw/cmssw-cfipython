import FWCore.ParameterSet.Config as cms

def CaloTowersClient(*args, **kwargs):
  mod = cms.EDProducer('CaloTowersClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
