import FWCore.ParameterSet.Config as cms

siPixelLorentzAnglePCLWorker = cms.EDProducer('SiPixelLorentzAnglePCLWorker',
  folder = cms.string('AlCaReco/SiPixelLorentzAngle'),
  notInPCL = cms.bool(False),
  fileName = cms.string('testrun.root'),
  newmodulelist = cms.vstring(),
  src = cms.InputTag('TrackRefitter'),
  ptMin = cms.double(3),
  normChi2Max = cms.double(2),
  clustSizeYMin = cms.int32(4),
  clustSizeYMinL4 = cms.int32(3),
  clustSizeXMax = cms.int32(5),
  residualMax = cms.double(0.005),
  clustChargeMaxPerLength = cms.double(50000),
  binsDepth = cms.int32(50),
  binsDrift = cms.int32(200),
  mightGet = cms.optional.untracked.vstring
)