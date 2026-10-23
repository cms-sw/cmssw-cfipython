import FWCore.ParameterSet.Config as cms

def HGCalWaferInfo(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalWaferInfo',
    detector = cms.string('HGCalEESensitive'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
