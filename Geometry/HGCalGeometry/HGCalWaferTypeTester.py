import FWCore.ParameterSet.Config as cms

def HGCalWaferTypeTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalWaferTypeTester',
    NameSense = cms.string('HGCalEESensitive'),
    NameDevice = cms.string('HGCal EE'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
