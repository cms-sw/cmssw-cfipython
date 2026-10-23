import FWCore.ParameterSet.Config as cms

def SimDoubletsProducerPhase2(*args, **kwargs):
  mod = cms.EDProducer('SimDoubletsProducerPhase2',
    clusterTPAssociationSrc = cms.InputTag('hltTPClusterProducer'),
    trackingParticleSrc = cms.InputTag('mix', 'MergedTrackTruth'),
    pixelRecHitSrc = cms.InputTag('hltSiPixelRecHits'),
    beamSpotSrc = cms.InputTag('hltOnlineBeamSpot'),
    TrackingParticleSelectionConfig = cms.PSet(
      ptMin = cms.double(0.9),
      ptMax = cms.double(1e+100),
      minRapidity = cms.double(-4.5),
      maxRapidity = cms.double(4.5),
      tip = cms.double(2),
      lip = cms.double(30),
      minHit = cms.int32(0),
      signalOnly = cms.bool(True),
      intimeOnly = cms.bool(False),
      chargedOnly = cms.bool(True),
      stableOnly = cms.bool(False),
      pdgId = cms.vint32(),
      invertRapidityCut = cms.bool(False),
      minPhi = cms.double(-3.2),
      maxPhi = cms.double(3.2)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
