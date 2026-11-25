import FWCore.ParameterSet.Config as cms

def MtdMergedClusterValidation(*args, **kwargs):
  mod = cms.EDProducer('MtdMergedClusterValidation',
    folder = cms.string('MTD/MergedClusters'),
    mergedClusters = cms.InputTag('mtdMergedClusters', 'FTLBarrel'),
    clusters = cms.InputTag('mtdClusters', 'FTLBarrel'),
    simMergedClusters = cms.InputTag('mtdSimMergedClusterProducer'),
    r2sAssociationMapTag = cms.InputTag('mtdRecoMergedClusterToSimMergedClusterAssociation'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
