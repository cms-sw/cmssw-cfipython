import FWCore.ParameterSet.Config as cms

def ElectronSeedConverter(*args, **kwargs):
  mod = cms.EDProducer('ElectronSeedConverter',
    initialSeeds = cms.InputTag('hltElePixelSeedsCombined'),
    eleSeedsSoA = cms.InputTag('ElectronNHitSeedAlpakaProducer'),
    superClusters = cms.InputTag('hltEgammaSuperClustersToPixelMatch'),
    beamSpot = cms.InputTag('hltOnlineBeamSpot'),
    measTkEvt = cms.InputTag('hltMeasurementTrackerEvent'),
    navSchool = cms.ESInputTag('', 'SimpleNavigationSchool'),
    detLayerGeom = cms.ESInputTag('', 'hltESPGlobalDetLayerGeometry'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
