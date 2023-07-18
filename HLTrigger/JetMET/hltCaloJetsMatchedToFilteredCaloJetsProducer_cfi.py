import FWCore.ParameterSet.Config as cms

hltCaloJetsMatchedToFilteredCaloJetsProducer = cms.EDProducer('HLTCaloJetsMatchedToFilteredCaloJetsProducer',
  src = cms.InputTag('hltJets'),
  triggerJetsFilter = cms.InputTag('hltCaloJetsFiltered'),
  triggerJetsType = cms.int32(85),
  maxDeltaR = cms.double(0.5),
  mightGet = cms.optional.untracked.vstring
)
