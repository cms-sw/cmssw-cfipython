import FWCore.ParameterSet.Config as cms

def HGCalWaferInFileCheck(**kwargs):
  mod = cms.EDAnalyzer('HGCalWaferInFileCheck',
    NameSense = cms.string('HGCalEESensitive'),
    NameDevice = cms.string('HGCal EE'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
