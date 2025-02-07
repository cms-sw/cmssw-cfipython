import FWCore.ParameterSet.Config as cms

def HGCalWaferInFileTest(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalWaferInFileTest',
    NameSense = cms.string('HGCalEESensitive'),
    NameDevice = cms.string('HGCal EE'),
    Verbosity = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
