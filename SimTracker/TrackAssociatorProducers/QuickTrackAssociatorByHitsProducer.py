import FWCore.ParameterSet.Config as cms

def QuickTrackAssociatorByHitsProducer(**kwargs):
  mod = cms.EDProducer('QuickTrackAssociatorByHitsProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
