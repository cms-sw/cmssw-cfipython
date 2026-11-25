import FWCore.ParameterSet.Config as cms

def MtdRecoMergedClusterToSimMergedClusterAssociatorByHitsProducer(*args, **kwargs):
  mod = cms.EDProducer('MtdRecoMergedClusterToSimMergedClusterAssociatorByHitsProducer',
    simToRecoMap = cms.InputTag('mtdRecoClusterToSimLayerClusterAssociation'),
    recoToSimMap = cms.InputTag('mtdRecoClusterToSimLayerClusterAssociation'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
