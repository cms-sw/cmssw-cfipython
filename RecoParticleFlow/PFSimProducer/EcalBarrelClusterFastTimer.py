import FWCore.ParameterSet.Config as cms

def EcalBarrelClusterFastTimer(*args, **kwargs):
  mod = cms.EDProducer('EcalBarrelClusterFastTimer',
    ecalDepth = cms.double(7),
    resolutionModels = cms.VPSet(
      cms.PSet(
        modelName = cms.string('PerfectResolutionModel')
      )
    ),
    timedVertices = cms.InputTag('offlinePrimaryVertices4D'),
    minFractionToConsider = cms.double(0.1),
    ebClusters = cms.InputTag('particleFlowClusterECALUncorrected'),
    minEnergyToConsider = cms.double(0),
    ebTimeHits = cms.InputTag('ecalDetailedTimeRecHit', 'EcalRecHitsEB'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
