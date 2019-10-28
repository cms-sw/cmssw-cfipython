import FWCore.ParameterSet.Config as cms

FastTrackDeDxProducer = cms.EDProducer('FastTrackDeDxProducer',
  estimator = cms.string('generic'),
  tracks = cms.InputTag('generalTracks'),
  UsePixel = cms.bool(False),
  UseStrip = cms.bool(True),
  MeVperADCStrip = cms.double(0.00095665000000000008),
  MeVperADCPixel = cms.double(3.61e-06),
  ShapeTest = cms.bool(True),
  UseCalibration = cms.bool(False),
  calibrationPath = cms.string(''),
  Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
  ProbabilityMode = cms.string('Accumulation'),
  fraction = cms.double(0.4),
  exponent = cms.double(-2),
  convertFromGeV2MeV = cms.bool(True),
  nothick = cms.bool(False),
  simHits = cms.required.InputTag,
  simHit2RecHitMap = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
