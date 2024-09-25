import FWCore.ParameterSet.Config as cms

def CaloTowersDQMClient(*args, **kwargs):
  mod = cms.EDProducer('CaloTowersDQMClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
