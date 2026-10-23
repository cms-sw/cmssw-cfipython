import FWCore.ParameterSet.Config as cms

def HGCalBadIdCheck(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalBadIdCheck',
    nameDetector = cms.string('HGCalEESensitive'),
    fileName = cms.string('D122FE.txt'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
