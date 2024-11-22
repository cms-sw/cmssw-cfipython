import FWCore.ParameterSet.Config as cms

def HGCalGeometryDump(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
