import FWCore.ParameterSet.Config as cms

def JetAnalyzer_HeavyIons_matching(**kwargs):
  mod = cms.EDProducer('JetAnalyzer_HeavyIons_matching',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
