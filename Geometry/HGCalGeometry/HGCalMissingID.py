import FWCore.ParameterSet.Config as cms

def HGCalMissingID(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalMissingID',
    nameDetectors = cms.vstring(
      'HGCalEESensitive',
      'HGCalHESiliconSensitive'
    ),
    fileName = cms.string('missingIDsV19.txt'),
    first = cms.int32(0),
    total = cms.int32(10),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
