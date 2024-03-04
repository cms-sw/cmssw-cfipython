import FWCore.ParameterSet.Config as cms

def HGCalTBGeometryDump(**kwargs):
  mod = cms.EDAnalyzer('HGCalTBGeometryDump',
    detectorNames = cms.vstring(
      'HGCalEESensitive',
      'HGCalHESiliconSensitive'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
