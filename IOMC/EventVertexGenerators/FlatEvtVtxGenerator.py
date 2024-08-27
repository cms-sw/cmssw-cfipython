import FWCore.ParameterSet.Config as cms

def FlatEvtVtxGenerator(**kwargs):
  mod = cms.EDProducer('FlatEvtVtxGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
