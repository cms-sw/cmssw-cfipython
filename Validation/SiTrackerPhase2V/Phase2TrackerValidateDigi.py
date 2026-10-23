import FWCore.ParameterSet.Config as cms

def Phase2TrackerValidateDigi(*args, **kwargs):
  mod = cms.EDProducer('Phase2TrackerValidateDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
