import FWCore.ParameterSet.Config as cms

def HGCalIdCheck(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalIdCheck',
    nameDetector = cms.string('HGCalHESiliconSensitive'),
    fileName = cms.string('D120E.txt'),
    outFileName = cms.string(''),
    mode = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
