import FWCore.ParameterSet.Config as cms

def EgammaHLTHGCalIDVarProducer(*args, **kwargs):
  mod = cms.EDProducer('EgammaHLTHGCalIDVarProducer',
    recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidate'),
    hgcalRecHits = cms.InputTag('hgcalRecHits'),
    layerClusters = cms.InputTag('layerClusters'),
    rCylinder = cms.double(2.7999999523162842),
    hOverECone = cms.double(0.15),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
