import FWCore.ParameterSet.Config as cms

def HGCalWaferCell(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalWaferCell',
    NameSense = cms.string('HGCalEESensitive'),
    NameDevice = cms.string('HGCal EE'),
    Verbosity = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
