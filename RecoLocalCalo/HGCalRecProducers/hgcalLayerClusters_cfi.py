import FWCore.ParameterSet.Config as cms

hgcalLayerClusters = cms.EDProducer('HGCalLayerClusterProducer',
  plugin = cms.PSet(
    thresholdW0 = cms.vdouble(
      2.9,
      2.9,
      2.9
    ),
    deltac = cms.vdouble(
      1.3,
      1.3,
      5,
      0.0315
    ),
    dependSensor = cms.bool(True),
    ecut = cms.double(3),
    kappa = cms.double(9),
    verbosity = cms.untracked.uint32(3),
    dEdXweights = cms.vdouble(),
    thicknessCorrection = cms.vdouble(),
    fcPerMip = cms.vdouble(),
    fcPerEle = cms.double(0),
    noises = cms.PSet(
      values = cms.vdouble()
    ),
    noiseMip = cms.PSet(
      scaleByDose = cms.bool(False),
      scaleByDoseAlgo = cms.uint32(0),
      doseMap = cms.string(''),
      noise_MIP = cms.double(0.01)
    ),
    use2x2 = cms.bool(True),
    type = cms.string('CLUE')
  
  ),
  detector = cms.string('all'),
  doSharing = cms.bool(False),
  HFNoseInput = cms.InputTag('HGCalRecHit', 'HGCHFNoseRecHits'),
  HGCEEInput = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
  HGCFHInput = cms.InputTag('HGCalRecHit', 'HGCHEFRecHits'),
  HGCBHInput = cms.InputTag('HGCalRecHit', 'HGCHEBRecHits'),
  timeClname = cms.string('timeLayerCluster'),
  timeOffset = cms.double(0),
  nHitsTime = cms.uint32(3),
  mightGet = cms.optional.untracked.vstring
)
