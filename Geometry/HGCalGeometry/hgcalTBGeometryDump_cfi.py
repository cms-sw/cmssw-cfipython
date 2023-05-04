import FWCore.ParameterSet.Config as cms

hgcalTBGeometryDump = cms.EDAnalyzer('HGCalTBGeometryDump',
  detectorNames = cms.vstring(
    'HGCalEESensitive',
    'HGCalHESiliconSensitive'
  ),
  mightGet = cms.optional.untracked.vstring
)
