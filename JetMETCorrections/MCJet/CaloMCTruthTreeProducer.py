import FWCore.ParameterSet.Config as cms

def CaloMCTruthTreeProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloMCTruthTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
