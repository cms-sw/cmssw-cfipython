import FWCore.ParameterSet.Config as cms

def HGCalWaferInFileTest(**kwargs):
  mod = cms.EDAnalyzer('HGCalWaferInFileTest',
    NameSense = cms.string('HGCalEESensitive'),
    NameDevice = cms.string('HGCal EE'),
    Verbosity = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
