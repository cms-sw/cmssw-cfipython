import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationAgainstCaloMuon = cms.EDProducer('PFRecoTauDiscriminationAgainstCaloMuon',
  srcHcalRecHits = cms.InputTag('hbhereco'),
  minLeadTrackPt = cms.double(15),
  maxEnToTrackRatio = cms.double(0.25),
  srcVertex = cms.InputTag('offlinePrimaryVertices'),
  PFTauProducer = cms.InputTag('pfRecoTauProducer'),
  srcEcalRecHitsBarrel = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
  dRhcal = cms.double(25),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet(
      cut = cms.required.double,
      Producer = cms.required.InputTag
    )
  ),
  maxEnHcal = cms.double(8),
  dRecal = cms.double(15),
  srcEcalRecHitsEndcap = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
  minLeadTrackPtFraction = cms.double(0.8),
  maxEnEcal = cms.double(3),
  mightGet = cms.optional.untracked.vstring
)
