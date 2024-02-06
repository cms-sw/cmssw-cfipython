import FWCore.ParameterSet.Config as cms

hgcalGeometryCheck = cms.EDAnalyzer('HGCalGeometryCheck',
  detectorNames = cms.vstring(
    'HGCalEESensitive',
    'HGCalHESiliconSensitive',
    'HGCalHEScintillatorSensitive'
  ),
  rMin = cms.untracked.double(0),
  rMax = cms.untracked.double(300),
  zMin = cms.untracked.double(300),
  zMax = cms.untracked.double(600),
  nBinR = cms.untracked.int32(300),
  nBinZ = cms.untracked.int32(600),
  ifNose = cms.untracked.bool(False),
  verbosity = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
