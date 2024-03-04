import FWCore.ParameterSet.Config as cms

def TrackerToMuonPropagator(**kwargs):
  mod = cms.EDProducer('TrackerToMuonPropagator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
