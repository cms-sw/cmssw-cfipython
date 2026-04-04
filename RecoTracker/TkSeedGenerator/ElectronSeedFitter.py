import FWCore.ParameterSet.Config as cms

def ElectronSeedFitter(*args, **kwargs):
  mod = cms.EDProducer('ElectronSeedFitter',
    eleSeedCollection = cms.InputTag('hltEgammaFittedElectronPixelSeeds'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    SeedMomentumForBOFF = cms.double(5),
    OriginTransverseErrorMultiplier = cms.double(1),
    MinOneOverPtError = cms.double(1),
    TTRHBuilder = cms.string('WithTrackAngle'),
    magneticField = cms.string('ParabolicMf'),
    beamSpot = cms.InputTag('hltOnlineBeamSpot'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
