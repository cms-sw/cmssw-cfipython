import FWCore.ParameterSet.Config as cms

hgcalLayerClusters = cms.EDProducer('HGCalLayerClusterProducer',
  detector = cms.string('all'),
  doSharing = cms.bool(False),
  thresholdW0 = cms.vdouble(
    2.9,
    2.9,
    2.9
  ),
  positionDeltaRho_c = cms.vdouble(
    1.3,
    1.3,
    1.3
  ),
  deltac = cms.vdouble(
    2,
    2,
    5
  ),
  dependSensor = cms.bool(True),
  ecut = cms.double(3),
  kappa = cms.double(9),
  timeClname = cms.string('timeLayerCluster'),
  timeOffset = cms.double(0),
  verbosity = cms.untracked.uint32(3),
  HGCEEInput = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
  HGCFHInput = cms.InputTag('HGCalRecHit', 'HGCHEFRecHits'),
  HGCBHInput = cms.InputTag('HGCalRecHit', 'HGCHEBRecHits'),
  dEdXweights = cms.vdouble(),
  thicknessCorrection = cms.vdouble(),
  fcPerMip = cms.vdouble(),
  fcPerEle = cms.double(0),
  noises = cms.PSet(
    values = cms.vdouble()
  ),
  noiseMip = cms.PSet(
    value = cms.double(0)
  )
)
