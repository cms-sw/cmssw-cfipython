import FWCore.ParameterSet.Config as cms

def CentralityTableProducer(**kwargs):
  mod = cms.EDAnalyzer('CentralityTableProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
