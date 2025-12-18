import FWCore.ParameterSet.Config as cms

def JetAnalyzer_HeavyIons_matching(*args, **kwargs):
  mod = cms.EDProducer('JetAnalyzer_HeavyIons_matching',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
