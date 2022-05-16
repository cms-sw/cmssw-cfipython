import FWCore.ParameterSet.Config as cms

hgcalGeometryDump = cms.EDAnalyzer('HGCalGeometryDump',
  detectorNames = cms.vstring(
    'HGCalEESensitive',
    'HGCalHESiliconSensitive',
    'HGCalHEScintillatorSensitive'
  ),
  detectorTypes = cms.vint32(
    0,
    0,
    1
  ),
  mightGet = cms.optional.untracked.vstring
)
