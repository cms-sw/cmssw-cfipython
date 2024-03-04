import FWCore.ParameterSet.Config as cms

def HGCalWaferTester(**kwargs):
  mod = cms.EDAnalyzer('HGCalWaferTester',
    NameSense = cms.string('HGCalEESensitive'),
    NameDevice = cms.string('HGCal EE'),
    Reco = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
