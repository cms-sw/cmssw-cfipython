import FWCore.ParameterSet.Config as cms

def HiHFFilterProducer(**kwargs):
  mod = cms.EDProducer('HiHFFilterProducer',
    srcTowers = cms.InputTag('towerMaker'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
