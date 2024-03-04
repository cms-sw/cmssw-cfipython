import FWCore.ParameterSet.Config as cms

def CollectionFromZLegProducer(**kwargs):
  mod = cms.EDProducer('CollectionFromZLegProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
