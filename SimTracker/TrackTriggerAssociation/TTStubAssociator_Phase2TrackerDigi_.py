import FWCore.ParameterSet.Config as cms

def TTStubAssociator_Phase2TrackerDigi_(*args, **kwargs):
  mod = cms.EDProducer('TTStubAssociator_Phase2TrackerDigi_',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
