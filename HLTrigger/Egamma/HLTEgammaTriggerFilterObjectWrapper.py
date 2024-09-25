import FWCore.ParameterSet.Config as cms

def HLTEgammaTriggerFilterObjectWrapper(*args, **kwargs):
  mod = cms.EDFilter('HLTEgammaTriggerFilterObjectWrapper',
    saveTags = cms.bool(True),
    candIsolatedTag = cms.InputTag('hltL1IsoRecoEcalCandidate'),
    candNonIsolatedTag = cms.InputTag('hltL1NonIsoRecoEcalCandidate'),
    doIsolated = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
