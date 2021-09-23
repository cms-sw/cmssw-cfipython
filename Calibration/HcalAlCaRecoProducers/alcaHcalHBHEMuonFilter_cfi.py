import FWCore.ParameterSet.Config as cms

alcaHcalHBHEMuonFilter = cms.EDFilter('AlCaHcalHBHEMuonFilter',
  prescale = cms.int32(1),
  hbheMuonLabel = cms.InputTag('alcaHcalHBHEMuonProducer', 'hbheMuon'),
  mightGet = cms.optional.untracked.vstring
)
