import FWCore.ParameterSet.Config as cms

def HGCalTestGuardRing(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalTestGuardRing',
    nameSense = cms.string('HGCalEESensitive'),
    waferFile = cms.string('testWafersEE.txt'),
    guardRingOffset = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
