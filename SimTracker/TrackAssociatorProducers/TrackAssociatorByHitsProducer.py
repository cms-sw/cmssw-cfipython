import FWCore.ParameterSet.Config as cms

def TrackAssociatorByHitsProducer(**kwargs):
  mod = cms.EDProducer('TrackAssociatorByHitsProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
