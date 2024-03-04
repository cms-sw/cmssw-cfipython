import FWCore.ParameterSet.Config as cms

def BeamProfileVtxGenerator(**kwargs):
  mod = cms.EDProducer('BeamProfileVtxGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
