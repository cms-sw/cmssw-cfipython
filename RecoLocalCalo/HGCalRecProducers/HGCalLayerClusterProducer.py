import FWCore.ParameterSet.Config as cms

def HGCalLayerClusterProducer(**kwargs):
  mod = cms.EDProducer('HGCalLayerClusterProducer',
    plugin = cms.PSet(
      thresholdW0 = cms.vdouble(
        2.9,
        2.9,
        2.9
      ),
      positionDeltaRho2 = cms.double(1.69),
      deltac = cms.vdouble(
        1.3,
        1.3,
        1.3,
        0.0315
      ),
      dependSensor = cms.bool(True),
      ecut = cms.double(3),
      kappa = cms.double(9),
      verbosity = cms.untracked.uint32(3),
      dEdXweights = cms.vdouble(),
      thicknessCorrection = cms.vdouble(),
      sciThicknessCorrection = cms.double(0.9),
      deltasi_index_regemfac = cms.int32(3),
      maxNumberOfThickIndices = cms.uint32(6),
      fcPerMip = cms.vdouble(),
      fcPerEle = cms.double(0),
      noises = cms.vdouble(),
      noiseMip = cms.PSet(
        scaleByDose = cms.bool(False),
        scaleByDoseAlgo = cms.uint32(0),
        scaleByDoseFactor = cms.double(1),
        doseMap = cms.string(''),
        sipmMap = cms.string(''),
        referenceIdark = cms.double(-1),
        referenceXtalk = cms.double(-1),
        noise_MIP = cms.double(0.01)
      ),
      use2x2 = cms.bool(True),
      type = cms.string('SiCLUE')
    
    ),
    detector = cms.string('EE'),
    recHits = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
    timeClname = cms.string('timeLayerCluster'),
    nHitsTime = cms.uint32(3),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
