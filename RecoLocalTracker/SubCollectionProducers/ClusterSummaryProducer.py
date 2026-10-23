import FWCore.ParameterSet.Config as cms

def ClusterSummaryProducer(*args, **kwargs):
  mod = cms.EDProducer('ClusterSummaryProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
