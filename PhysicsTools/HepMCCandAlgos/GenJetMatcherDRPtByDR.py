import FWCore.ParameterSet.Config as cms

def GenJetMatcherDRPtByDR(**kwargs):
  mod = cms.EDProducer('GenJetMatcherDRPtByDR',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
