import FWCore.ParameterSet.Config as cms

def MtdSimLayerClusterToTPAssociatorByTrackIdProducer(**kwargs):
  mod = cms.EDProducer('MtdSimLayerClusterToTPAssociatorByTrackIdProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
