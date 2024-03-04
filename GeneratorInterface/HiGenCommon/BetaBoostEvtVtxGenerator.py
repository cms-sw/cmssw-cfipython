import FWCore.ParameterSet.Config as cms

def BetaBoostEvtVtxGenerator(**kwargs):
  mod = cms.EDProducer('BetaBoostEvtVtxGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
