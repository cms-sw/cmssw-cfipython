import FWCore.ParameterSet.Config as cms

def TrackAssociatorByPositionProducer(**kwargs):
  mod = cms.EDProducer('TrackAssociatorByPositionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
