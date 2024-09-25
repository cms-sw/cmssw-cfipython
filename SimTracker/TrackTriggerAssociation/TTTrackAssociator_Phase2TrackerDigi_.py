import FWCore.ParameterSet.Config as cms

def TTTrackAssociator_Phase2TrackerDigi_(*args, **kwargs):
  mod = cms.EDProducer('TTTrackAssociator_Phase2TrackerDigi_',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
