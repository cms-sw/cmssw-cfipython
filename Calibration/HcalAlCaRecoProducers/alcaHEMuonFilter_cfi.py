import FWCore.ParameterSet.Config as cms

alcaHEMuonFilter = cms.EDFilter('AlCaHEMuonFilter',
  processName = cms.string('HLT'),
  triggerResultLabel = cms.InputTag('TriggerResults', '', 'HLT'),
  muonLabel = cms.InputTag('muons'),
  minimumMuonP = cms.double(10),
  triggers = cms.vstring(
    'HLT_IsoMu',
    'HLT_Mu'
  ),
  muonPtCut = cms.double(20),
  muonEtaCut = cms.double(1.305),
  pfCut = cms.bool(True),
  pfIsolationCut = cms.double(0.15),
  trackIsolationCut = cms.double(3),
  caloIsolationCut = cms.double(5),
  preScale = cms.int32(1),
  mightGet = cms.optional.untracked.vstring
)
