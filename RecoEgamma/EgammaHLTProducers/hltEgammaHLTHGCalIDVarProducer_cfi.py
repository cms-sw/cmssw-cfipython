import FWCore.ParameterSet.Config as cms

hltEgammaHLTHGCalIDVarProducer = cms.EDProducer('EgammaHLTHGCalIDVarProducer',
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidate'),
  hgcalRecHits = cms.InputTag('hgcalRecHits'),
  layerClusters = cms.InputTag('layerClusters'),
  rCylinder = cms.double(2.8),
  hOverECone = cms.double(0.15),
  mightGet = cms.optional.untracked.vstring
)
