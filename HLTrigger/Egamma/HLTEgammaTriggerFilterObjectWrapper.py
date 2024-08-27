import FWCore.ParameterSet.Config as cms

def HLTEgammaTriggerFilterObjectWrapper(**kwargs):
  mod = cms.EDFilter('HLTEgammaTriggerFilterObjectWrapper',
    saveTags = cms.bool(True),
    candIsolatedTag = cms.InputTag('hltL1IsoRecoEcalCandidate'),
    candNonIsolatedTag = cms.InputTag('hltL1NonIsoRecoEcalCandidate'),
    doIsolated = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
