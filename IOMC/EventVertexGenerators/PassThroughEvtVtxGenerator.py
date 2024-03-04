import FWCore.ParameterSet.Config as cms

def PassThroughEvtVtxGenerator(**kwargs):
  mod = cms.EDProducer('PassThroughEvtVtxGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
