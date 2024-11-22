import FWCore.ParameterSet.Config as cms

def Multi5x5ClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('Multi5x5ClusterProducer',
    barrelHitTag = cms.required.InputTag,
    endcapHitTag = cms.required.InputTag,
    doEndcap = cms.required.bool,
    doBarrel = cms.required.bool,
    barrelClusterCollection = cms.required.string,
    endcapClusterCollection = cms.required.string,
    IslandBarrelSeedThr = cms.required.double,
    IslandEndcapSeedThr = cms.required.double,
    RecHitFlagToBeExcluded = cms.required.vstring,
    posCalcParameters = cms.PSet(
      LogWeighted = cms.required.bool,
      T0_barl = cms.required.double,
      T0_endc = cms.required.double,
      T0_endcPresh = cms.required.double,
      W0 = cms.required.double,
      X0 = cms.required.double
    ),
    reassignSeedCrysToClusterItSeeds = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
