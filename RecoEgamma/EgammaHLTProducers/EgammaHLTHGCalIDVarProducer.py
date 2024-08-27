import FWCore.ParameterSet.Config as cms

def EgammaHLTHGCalIDVarProducer(**kwargs):
  mod = cms.EDProducer('EgammaHLTHGCalIDVarProducer',
    recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidate'),
    hgcalRecHits = cms.InputTag('hgcalRecHits'),
    layerClusters = cms.InputTag('layerClusters'),
    rCylinder = cms.double(2.7999999523162842),
    hOverECone = cms.double(0.15),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
