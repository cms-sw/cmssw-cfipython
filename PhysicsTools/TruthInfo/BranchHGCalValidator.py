import FWCore.ParameterSet.Config as cms

def BranchHGCalValidator(*args, **kwargs):
  mod = cms.EDProducer('BranchHGCalValidator',
    src = cms.InputTag('truthLogicalGraphProducer'),
    rawSrc = cms.InputTag('truthGraphProducer'),
    hitIndex = cms.InputTag('truthLogicalGraphHitIndexProducer'),
    caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
    simClusters = cms.InputTag('mix', 'MergedCaloTruth'),
    folder = cms.string('HGCAL/BranchValidator'),
    minPt = cms.double(1),
    maxEta = cms.double(3),
    hgcalRecHits = cms.VInputTag(
      'HGCalRecHit:HGCEERecHits',
      'HGCalRecHit:HGCHEFRecHits',
      'HGCalRecHit:HGCHEBRecHits'
    ),
    pfRecHits = cms.VInputTag(
      'particleFlowRecHitECAL:Cleaned',
      'particleFlowRecHitHBHE:Cleaned',
      'particleFlowRecHitHF:Cleaned',
      'particleFlowRecHitHO:Cleaned'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
