import FWCore.ParameterSet.Config as cms

def HGCalCellSizeHexTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalCellSizeHexTester',
    nameDetectors = cms.vstring(
      'HGCalEESensitive',
      'HGCalHESiliconSensitive'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
