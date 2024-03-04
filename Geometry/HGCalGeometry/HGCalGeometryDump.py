import FWCore.ParameterSet.Config as cms

def HGCalGeometryDump(**kwargs):
  mod = cms.EDAnalyzer('HGCalGeometryDump',
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
