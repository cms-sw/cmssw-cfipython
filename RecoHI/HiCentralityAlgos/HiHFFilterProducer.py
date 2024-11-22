import FWCore.ParameterSet.Config as cms

def HiHFFilterProducer(*args, **kwargs):
  mod = cms.EDProducer('HiHFFilterProducer',
    srcTowers = cms.InputTag('towerMaker'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
