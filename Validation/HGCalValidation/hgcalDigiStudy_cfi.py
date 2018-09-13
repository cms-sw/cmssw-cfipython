import FWCore.ParameterSet.Config as cms

hgcalDigiStudy = cms.EDAnalyzer('HGCalDigiStudy',
  detectorNames = cms.vstring(
    'HGCalEESensitive',
    'HGCalHESiliconSensitive',
    'Hcal'
  ),
  DigiSources = cms.VInputTag(
    'simHGCalUnsuppressedlDigis:EE',
    'simHGCalUnsuppressedlDigis:HEfront',
    'simHGCalUnsuppressedlDigis:HEback'
  ),
  ifNose = cms.untracked.bool(False),
  ifHCAL = cms.untracked.bool(False),
  verbosity = cms.untracked.int32(0),
  sampleIndex = cms.untracked.int32(0),
  rMin = cms.untracked.double(0),
  rMax = cms.untracked.double(3000),
  zMin = cms.untracked.double(3000),
  zMax = cms.untracked.double(6000),
  nBinR = cms.untracked.int32(300),
  nBinZ = cms.untracked.int32(300)
)
