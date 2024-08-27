import FWCore.ParameterSet.Config as cms

def ClusterSummaryProducer(**kwargs):
  mod = cms.EDProducer('ClusterSummaryProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
