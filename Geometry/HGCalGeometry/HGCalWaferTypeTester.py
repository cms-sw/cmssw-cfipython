import FWCore.ParameterSet.Config as cms

def HGCalWaferTypeTester(**kwargs):
  mod = cms.EDAnalyzer('HGCalWaferTypeTester',
    NameSense = cms.string('HGCalEESensitive'),
    NameDevice = cms.string('HGCal EE'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
