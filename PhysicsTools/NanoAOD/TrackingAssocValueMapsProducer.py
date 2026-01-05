import FWCore.ParameterSet.Config as cms

def TrackingAssocValueMapsProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackingAssocValueMapsProducer',
    trackCollection = cms.InputTag('generalTracks'),
    associator = cms.InputTag('trackingParticleRecoTrackAsssociation'),
    trackingParticles = cms.InputTag('mix', 'MergedTrackTruth'),
    tpSelectorPSet = cms.PSet(
      ptMin = cms.double(0.005),
      ptMax = cms.double(1e+100),
      minRapidity = cms.double(-2.5),
      maxRapidity = cms.double(2.5),
      tip = cms.double(60),
      lip = cms.double(30),
      minHit = cms.int32(0),
      signalOnly = cms.bool(False),
      intimeOnly = cms.bool(True),
      chargedOnly = cms.bool(True),
      stableOnly = cms.bool(False),
      pdgId = cms.vint32(),
      invertRapidityCut = cms.bool(False),
      minPhi = cms.double(-3.2),
      maxPhi = cms.double(3.2)
    ),
    storeTPKinematics = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
