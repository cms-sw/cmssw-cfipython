import FWCore.ParameterSet.Config as cms

def HGCalIdCheck(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalIdCheck',
    nameDetectors = cms.vstring(
      'HGCalEESensitive',
      'HGCalHESiliconSensitive'
    ),
    fileName = cms.string('D120E.txt'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
