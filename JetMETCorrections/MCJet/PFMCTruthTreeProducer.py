import FWCore.ParameterSet.Config as cms

def PFMCTruthTreeProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('PFMCTruthTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
