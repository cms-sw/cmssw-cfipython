import FWCore.ParameterSet.Config as cms

def Pi0FixedMassWindowCalibration(**kwargs):
  mod = cms.Looper('Pi0FixedMassWindowCalibration',
    maxLoops = cms.uint32(0),
    ecalRecHitsProducer = cms.string(''),
    barrelHitCollection = cms.string(''),
    VerbosityLevel = cms.string(''),
    barrelClusterCollection = cms.string(''),
    IslandBarrelSeedThr = cms.double(0),
    IslandEndcapSeedThr = cms.double(0),
    selePi0PtGammaOneMin = cms.double(0),
    selePi0PtGammaTwoMin = cms.double(0),
    selePi0DRBelt = cms.double(0),
    selePi0DetaBelt = cms.double(0),
    selePi0PtPi0Min = cms.double(0),
    selePi0S4S9GammaOneMin = cms.double(0),
    selePi0S4S9GammaTwoMin = cms.double(0),
    selePi0S9S25GammaOneMin = cms.double(0),
    selePi0S9S25GammaTwoMin = cms.double(0),
    selePi0EtBeltIsoRatioMax = cms.double(0),
    selePi0MinvMeanFixed = cms.double(0),
    selePi0MinvSigmaFixed = cms.double(0),
    posCalcParameters = cms.PSet(
      LogWeighted = cms.bool(True),
      T0_barl = cms.double(7.4),
      T0_endc = cms.double(3.1),
      T0_endcPresh = cms.double(1.2),
      W0 = cms.double(4.2),
      X0 = cms.double(0.89)
    ),
    clustershapecollectionEB = cms.string('islandBarrelShape'),
    barrelShapeAssociation = cms.string('islandBarrelShapeAssoc'),
    SeedRecHitFlagToBeExcludedEB = cms.vstring(),
    SeedRecHitFlagToBeExcludedEE = cms.vstring(),
    RecHitFlagToBeExcludedEB = cms.vstring(),
    RecHitFlagToBeExcludedEE = cms.vstring(),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod