import FWCore.ParameterSet.Config as cms

hltpfJetsMatchedToFilteredPFJetsProducer = cms.EDProducer('HLTPFJetsMatchedToFilteredPFJetsProducer',
  src = cms.InputTag('hltJets'),
  triggerJetsFilter = cms.InputTag('hltCaloJetsFiltered'),
  triggerJetsType = cms.int32(85),
  maxDeltaR = cms.double(0.5),
  mightGet = cms.optional.untracked.vstring
)
