import FWCore.ParameterSet.Config as cms

AlcaHBHEMuonFilter = cms.EDFilter('AlCaHBHEMuonFilter',
  ProcessName = cms.string('HLT'),
  TriggerResultLabel = cms.InputTag('TriggerResults', '', 'HLT'),
  MuonLabel = cms.InputTag('muons'),
  MinimumMuonP = cms.double(5),
  Triggers = cms.vstring(
    'HLT_IsoMu',
    'HLT_Mu'
  ),
  PFCut = cms.bool(True),
  PFIsolationCut = cms.double(0.12),
  TrackIsolationCut = cms.double(3),
  CaloIsolationCut = cms.double(5),
  PreScale = cms.int32(2),
  OnlyOuterTrack = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
