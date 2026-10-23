import FWCore.ParameterSet.Config as cms

def PassThroughEvtVtxGenerator(*args, **kwargs):
  mod = cms.EDProducer('PassThroughEvtVtxGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
