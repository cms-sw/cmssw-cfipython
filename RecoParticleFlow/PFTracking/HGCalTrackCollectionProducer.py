import FWCore.ParameterSet.Config as cms

def HGCalTrackCollectionProducer(**kwargs):
  mod = cms.EDProducer('HGCalTrackCollectionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
