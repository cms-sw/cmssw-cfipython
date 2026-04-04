import FWCore.ParameterSet.Config as cms

def BarrelLayerClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('BarrelLayerClusterProducer',
    plugin = cms.PSet(
      outlierDeltaFactor = cms.double(2),
      kappa = cms.double(1.34),
      maxLayerIndex = cms.int32(0),
      deltac = cms.double(0.0175),
      fractionCutoff = cms.double(0),
      doSharing = cms.bool(False),
      type = cms.string('EBCLUE')
    
    ),
    recHits = cms.InputTag('particleFlowRecHitECAL'),
    timeResolutionCalc = cms.PSet(
      noiseTerm = cms.double(1.10889),
      constantTerm = cms.double(0.428192),
      corrTermLowE = cms.double(0.0510871),
      threshLowE = cms.double(0.5),
      constantTermLowE = cms.double(0),
      noiseTermLowE = cms.double(1.31883),
      threshHighE = cms.double(5)
    ),
    timeClname = cms.string('timeLayerCluster'),
    nHitsTime = cms.uint32(3),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
