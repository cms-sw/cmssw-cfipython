import FWCore.ParameterSet.Config as cms

def MixBoostEvtVtxGenerator(**kwargs):
  mod = cms.EDProducer('MixBoostEvtVtxGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
