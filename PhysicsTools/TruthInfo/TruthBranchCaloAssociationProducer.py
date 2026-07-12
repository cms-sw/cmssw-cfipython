import FWCore.ParameterSet.Config as cms

def TruthBranchCaloAssociationProducer(*args, **kwargs):
  mod = cms.EDProducer('TruthBranchCaloAssociationProducer',
    src = cms.InputTag('truthLogicalGraphProducer'),
    hitIndex = cms.InputTag('truthLogicalGraphHitIndexProducer'),
    caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
    simClusters = cms.InputTag('mix', 'MergedCaloTruth'),
    interestingPdgIds = cms.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
