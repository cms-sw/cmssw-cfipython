import FWCore.ParameterSet.Config as cms

def FromClusterSummaryMultiplicityProducer(**kwargs):
  mod = cms.EDProducer('FromClusterSummaryMultiplicityProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
