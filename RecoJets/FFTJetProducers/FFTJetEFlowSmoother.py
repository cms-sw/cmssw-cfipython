import FWCore.ParameterSet.Config as cms

def FFTJetEFlowSmoother(*args, **kwargs):
  mod = cms.EDProducer('FFTJetEFlowSmoother',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
