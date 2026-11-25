import FWCore.ParameterSet.Config as cms

def MtdSimMergedClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('MtdSimMergedClusterProducer',
    trackingParticles = cms.InputTag('mix', 'MergedTrackTruth'),
    mtdSimLayerClusters = cms.InputTag('mix', 'MergedMtdTruthLC'),
    tp2SimAssociationMap = cms.InputTag('mtdSimLayerClusterToTPAssociation'),
    minClusterEnergy = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
