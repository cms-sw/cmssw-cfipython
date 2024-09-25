import FWCore.ParameterSet.Config as cms

def BeamHaloProducer(*args, **kwargs):
  mod = cms.EDProducer('BeamHaloProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
