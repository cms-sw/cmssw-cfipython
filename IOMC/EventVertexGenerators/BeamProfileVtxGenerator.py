import FWCore.ParameterSet.Config as cms

def BeamProfileVtxGenerator(*args, **kwargs):
  mod = cms.EDProducer('BeamProfileVtxGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
