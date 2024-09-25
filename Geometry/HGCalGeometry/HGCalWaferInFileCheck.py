import FWCore.ParameterSet.Config as cms

def HGCalWaferInFileCheck(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalWaferInFileCheck',
    NameSense = cms.string('HGCalEESensitive'),
    NameDevice = cms.string('HGCal EE'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
