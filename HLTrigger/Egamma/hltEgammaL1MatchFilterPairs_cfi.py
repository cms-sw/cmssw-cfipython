import FWCore.ParameterSet.Config as cms

hltEgammaL1MatchFilterPairs = cms.EDFilter('HLTEgammaL1MatchFilterPairs',
  saveTags = cms.bool(True),
  candIsolatedTag = cms.InputTag('hltRecoIsolatedEcalCandidate'),
  l1IsolatedTag = cms.InputTag('l1extraParticles', 'Isolated'),
  candNonIsolatedTag = cms.InputTag('hltRecoNonIsolatedEcalCandidate'),
  l1NonIsolatedTag = cms.InputTag('l1extraParticles', 'NonIsolated'),
  L1SeedFilterTag = cms.InputTag('theL1SeedFilter'),
  AlsoNonIsolatedFirst = cms.bool(False),
  AlsoNonIsolatedSecond = cms.bool(False),
  region_eta_size = cms.double(0.522),
  region_eta_size_ecap = cms.double(1),
  region_phi_size = cms.double(1.044),
  barrel_end = cms.double(1.4791),
  endcap_end = cms.double(2.65)
)
