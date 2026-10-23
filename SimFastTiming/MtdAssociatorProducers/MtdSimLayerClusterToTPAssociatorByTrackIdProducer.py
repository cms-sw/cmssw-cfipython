import FWCore.ParameterSet.Config as cms

def MtdSimLayerClusterToTPAssociatorByTrackIdProducer(*args, **kwargs):
  mod = cms.EDProducer('MtdSimLayerClusterToTPAssociatorByTrackIdProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
