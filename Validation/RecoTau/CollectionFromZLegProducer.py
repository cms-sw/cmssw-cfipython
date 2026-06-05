import FWCore.ParameterSet.Config as cms

def CollectionFromZLegProducer(*args, **kwargs):
  mod = cms.EDProducer('CollectionFromZLegProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
