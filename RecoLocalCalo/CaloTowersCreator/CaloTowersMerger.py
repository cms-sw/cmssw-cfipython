import FWCore.ParameterSet.Config as cms

def CaloTowersMerger(*args, **kwargs):
  mod = cms.EDProducer('CaloTowersMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
