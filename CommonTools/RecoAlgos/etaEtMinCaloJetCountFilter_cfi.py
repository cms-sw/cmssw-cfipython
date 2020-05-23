import FWCore.ParameterSet.Config as cms

etaEtMinCaloJetCountFilter = cms.EDFilter('EtaEtMinCaloJetCountFilter',
  src = cms.InputTag(''),
  etMin = cms.double(0),
  etaMin = cms.double(0),
  etaMax = cms.double(0),
  minNumber = cms.uint32(0),
  mightGet = cms.optional.untracked.vstring
)
