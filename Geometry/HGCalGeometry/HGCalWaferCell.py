import FWCore.ParameterSet.Config as cms

def HGCalWaferCell(**kwargs):
  mod = cms.EDAnalyzer('HGCalWaferCell',
    NameSense = cms.string('HGCalEESensitive'),
    NameDevice = cms.string('HGCal EE'),
    Verbosity = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
