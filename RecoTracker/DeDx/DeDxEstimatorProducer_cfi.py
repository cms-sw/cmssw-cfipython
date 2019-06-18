import FWCore.ParameterSet.Config as cms

DeDxEstimatorProducer = cms.EDProducer('DeDxEstimatorProducer',
  estimator = cms.string('generic'),
  tracks = cms.InputTag('generalTracks'),
  UsePixel = cms.bool(False),
  UseStrip = cms.bool(True),
  MeVperADCPixel = cms.double(3.61e-06),
  MeVperADCStrip = cms.double(0.00095665000000000008),
  ShapeTest = cms.bool(True),
  UseCalibration = cms.bool(False),
  calibrationPath = cms.string(''),
  Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
  ProbabilityMode = cms.string('Accumulation'),
  fraction = cms.double(0.4),
  exponent = cms.double(-2),
  mightGet = cms.optional.untracked.vstring
)
