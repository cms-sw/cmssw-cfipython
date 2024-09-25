import FWCore.ParameterSet.Config as cms

def FlatEvtVtxGenerator(*args, **kwargs):
  mod = cms.EDProducer('FlatEvtVtxGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
