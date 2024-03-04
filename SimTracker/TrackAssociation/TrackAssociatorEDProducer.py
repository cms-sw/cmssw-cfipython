import FWCore.ParameterSet.Config as cms

def TrackAssociatorEDProducer(**kwargs):
  mod = cms.EDProducer('TrackAssociatorEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
