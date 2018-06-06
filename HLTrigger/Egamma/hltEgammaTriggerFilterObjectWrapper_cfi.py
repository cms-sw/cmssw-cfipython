import FWCore.ParameterSet.Config as cms

hltEgammaTriggerFilterObjectWrapper = cms.EDFilter('HLTEgammaTriggerFilterObjectWrapper',
  saveTags = cms.bool(True),
  candIsolatedTag = cms.InputTag('hltL1IsoRecoEcalCandidate'),
  candNonIsolatedTag = cms.InputTag('hltL1NonIsoRecoEcalCandidate'),
  doIsolated = cms.bool(False)
)
