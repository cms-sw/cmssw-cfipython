import FWCore.ParameterSet.Config as cms

def HLTEcalTowerFilter(**kwargs):
  mod = cms.EDFilter('HLTEcalTowerFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltTowerMakerForEcal'),
    MinE = cms.double(10),
    MaxEta = cms.double(3),
    MinN = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
