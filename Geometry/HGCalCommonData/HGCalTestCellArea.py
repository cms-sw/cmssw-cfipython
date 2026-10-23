import FWCore.ParameterSet.Config as cms

def HGCalTestCellArea(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalTestCellArea',
    nameDetectors = cms.vstring(
      'HGCalEESensitive',
      'HGCalHESiliconSensitive'
    ),
    fileName = cms.string('missD88.txt'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
