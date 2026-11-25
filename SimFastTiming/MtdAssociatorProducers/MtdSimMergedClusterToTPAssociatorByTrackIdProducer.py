import FWCore.ParameterSet.Config as cms

def MtdSimMergedClusterToTPAssociatorByTrackIdProducer(*args, **kwargs):
  mod = cms.EDProducer('MtdSimMergedClusterToTPAssociatorByTrackIdProducer',
    simToTPMap = cms.InputTag('mtdSimLayerClusterToTPAssociation'),
    tpToSimMap = cms.InputTag('mtdSimLayerClusterToTPAssociation'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
