import FWCore.ParameterSet.Config as cms

def HGCalTestDDDCons(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalTestDDDCons',
    nameDetectors = cms.vstring(
      'HGCalEESensitive',
      'HGCalHESiliconSensitive'
    ),
    fileName = cms.string('missD120.txt'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
