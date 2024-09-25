import FWCore.ParameterSet.Config as cms

def HLTEcalTowerFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTEcalTowerFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltTowerMakerForEcal'),
    MinE = cms.double(10),
    MaxEta = cms.double(3),
    MinN = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
