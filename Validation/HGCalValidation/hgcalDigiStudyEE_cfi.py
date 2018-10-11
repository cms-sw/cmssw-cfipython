import FWCore.ParameterSet.Config as cms

hgcalDigiStudyEE = cms.EDAnalyzer('HGCalDigiStudy',
  detectorName = cms.string('HGCalEESensitive'),
  digiSource = cms.InputTag('hgcalDigis', 'EE'),
  ifNose = cms.untracked.bool(False),
  ifHCAL = cms.untracked.bool(False),
  verbosity = cms.untracked.int32(0),
  sampleIndex = cms.untracked.int32(0),
  rMin = cms.untracked.double(0),
  rMax = cms.untracked.double(300),
  zMin = cms.untracked.double(300),
  zMax = cms.untracked.double(600),
  nBinR = cms.untracked.int32(300),
  nBinZ = cms.untracked.int32(300)
)
