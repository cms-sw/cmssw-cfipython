import FWCore.ParameterSet.Config as cms

def GenJetMatcherDRPtByDR(*args, **kwargs):
  mod = cms.EDProducer('GenJetMatcherDRPtByDR',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
