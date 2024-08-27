import FWCore.ParameterSet.Config as cms

def JetAnalyzer(**kwargs):
  mod = cms.EDProducer('JetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
