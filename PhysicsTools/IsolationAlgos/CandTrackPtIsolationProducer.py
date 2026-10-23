import FWCore.ParameterSet.Config as cms

def CandTrackPtIsolationProducer(*args, **kwargs):
  mod = cms.EDProducer('CandTrackPtIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
