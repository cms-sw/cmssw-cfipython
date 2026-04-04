import FWCore.ParameterSet.Config as cms

def HGCalWaferTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalWaferTester',
    NameSense = cms.string('HGCalEESensitive'),
    NameDevice = cms.string('HGCal EE'),
    Reco = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
