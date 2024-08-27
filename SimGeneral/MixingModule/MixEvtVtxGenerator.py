import FWCore.ParameterSet.Config as cms

def MixEvtVtxGenerator(**kwargs):
  mod = cms.EDProducer('MixEvtVtxGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
