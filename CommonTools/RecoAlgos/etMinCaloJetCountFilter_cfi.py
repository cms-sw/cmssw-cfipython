import FWCore.ParameterSet.Config as cms

etMinCaloJetCountFilter = cms.EDFilter('EtMinCaloJetCountFilter',
  src = cms.InputTag(''),
  etMin = cms.double(0),
  minNumber = cms.uint32(0),
  mightGet = cms.optional.untracked.vstring
)
