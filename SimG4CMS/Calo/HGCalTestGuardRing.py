import FWCore.ParameterSet.Config as cms

def HGCalTestGuardRing(**kwargs):
  mod = cms.EDAnalyzer('HGCalTestGuardRing',
    nameSense = cms.string('HGCalEESensitive'),
    waferFile = cms.string('testWafersEE.txt'),
    guardRingOffset = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
