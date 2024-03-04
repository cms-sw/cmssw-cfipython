import FWCore.ParameterSet.Config as cms

def HLTCaloTowerFilter(**kwargs):
  mod = cms.EDFilter('HLTCaloTowerFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltTowerMakerForEcal'),
    MinPt = cms.double(3),
    MaxEta = cms.double(3),
    MinN = cms.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
