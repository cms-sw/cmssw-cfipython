import FWCore.ParameterSet.Config as cms

def BetaBoostEvtVtxGenerator(*args, **kwargs):
  mod = cms.EDProducer('BetaBoostEvtVtxGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
