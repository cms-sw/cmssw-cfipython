import FWCore.ParameterSet.Config as cms

def MixEvtVtxGenerator(*args, **kwargs):
  mod = cms.EDProducer('MixEvtVtxGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
