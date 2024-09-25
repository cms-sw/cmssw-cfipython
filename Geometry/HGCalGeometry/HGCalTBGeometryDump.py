import FWCore.ParameterSet.Config as cms

def HGCalTBGeometryDump(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalTBGeometryDump',
    detectorNames = cms.vstring(
      'HGCalEESensitive',
      'HGCalHESiliconSensitive'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
