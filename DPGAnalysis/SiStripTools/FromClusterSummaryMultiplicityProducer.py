import FWCore.ParameterSet.Config as cms

def FromClusterSummaryMultiplicityProducer(*args, **kwargs):
  mod = cms.EDProducer('FromClusterSummaryMultiplicityProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
