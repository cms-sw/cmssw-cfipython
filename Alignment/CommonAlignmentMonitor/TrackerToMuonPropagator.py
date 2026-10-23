import FWCore.ParameterSet.Config as cms

def TrackerToMuonPropagator(*args, **kwargs):
  mod = cms.EDProducer('TrackerToMuonPropagator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
