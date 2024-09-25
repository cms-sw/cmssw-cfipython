import FWCore.ParameterSet.Config as cms

def QuickTrackAssociatorByHitsProducer(*args, **kwargs):
  mod = cms.EDProducer('QuickTrackAssociatorByHitsProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
