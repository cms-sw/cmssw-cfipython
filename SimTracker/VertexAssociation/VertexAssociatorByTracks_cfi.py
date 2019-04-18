import FWCore.ParameterSet.Config as cms

VertexAssociatorByTracks = cms.EDProducer('VertexAssociatorByTracksProducer',
  R2SMatchedSimRatio = cms.double(0.3),
  R2SMatchedRecoRatio = cms.double(0),
  S2RMatchedSimRatio = cms.double(0),
  S2RMatchedRecoRatio = cms.double(0.3),
  trackQuality = cms.string('highPurity'),
  trackingParticleSelector = cms.PSet(
    lipTP = cms.double(30),
    chargedOnlyTP = cms.bool(True),
    pdgIdTP = cms.vint32(),
    signalOnlyTP = cms.bool(True),
    minRapidityTP = cms.double(-2.4),
    minHitTP = cms.int32(0),
    ptMinTP = cms.double(0.9),
    maxRapidityTP = cms.double(2.4),
    tipTP = cms.double(3.5)
  ),
  trackAssociation = cms.InputTag('trackingParticleRecoTrackAsssociation')
)
